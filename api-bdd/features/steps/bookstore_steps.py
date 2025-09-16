
from http import HTTPStatus
from behave import given, when, then

@given("que eu possuo credenciais válidas")
def step_impl_creds(context):
    assert "userName" in context.creds and "password" in context.creds

@when("eu crio um novo usuário")
def step_impl_create_user(context):
    url = f"{context.base_url}/Account/v1/User"
    resp = context.session.post(url, json=context.creds)
    assert resp.status_code in (HTTPStatus.OK, HTTPStatus.CREATED), resp.text
    body = resp.json()
    context.state["user_id"] = body.get("userID") or body.get("userId")
    assert context.state["user_id"], f"userID ausente: {body}"

@when("eu gero um token de acesso")
def step_impl_token(context):
    url = f"{context.base_url}/Account/v1/GenerateToken"
    resp = context.session.post(url, json=context.creds)
    assert resp.status_code == HTTPStatus.OK, resp.text
    token = resp.json().get("token")
    assert token, resp.json()
    context.session.headers.update({"Authorization": f"Bearer {token}"})

@when("eu verifico a autorização do usuário")
def step_impl_authorized(context):
    url = f"{context.base_url}/Account/v1/Authorized"
    resp = context.session.post(url, json=context.creds)
    assert resp.status_code == HTTPStatus.OK, resp.text
    assert resp.json() is True, resp.text

@when("eu consulto a lista de livros disponíveis")
def step_impl_list_books(context):
    url = f"{context.base_url}/BookStore/v1/Books"
    resp = context.session.get(url)
    assert resp.status_code == HTTPStatus.OK, resp.text
    books = resp.json().get("books", [])
    assert len(books) >= 2, "Menos de dois livros para selecionar"
    context.state["isbns"] = [books[0]["isbn"], books[1]["isbn"]]

@when("eu adiciono dois livros ao usuário")
def step_impl_add_books(context):
    user_id = context.state["user_id"]
    isbns = context.state["isbns"]
    url = f"{context.base_url}/BookStore/v1/Books"
    payload = {"userId": user_id, "collectionOfIsbns": [{"isbn": i} for i in isbns]}
    resp = context.session.post(url, json=payload)
    assert resp.status_code in (HTTPStatus.OK, HTTPStatus.CREATED), resp.text

@then("o usuário deve conter exatamente esses dois livros")
def step_impl_validate_user(context):
    user_id = context.state["user_id"]
    isbns = sorted(context.state["isbns"])
    url = f"{context.base_url}/Account/v1/User/{user_id}"
    resp = context.session.get(url)
    assert resp.status_code == HTTPStatus.OK, resp.text
    body = resp.json()
    returned_isbns = sorted([b.get("isbn") for b in body.get("books", [])])
    assert returned_isbns == isbns, f"Esperado {isbns}, recebido {returned_isbns}"
