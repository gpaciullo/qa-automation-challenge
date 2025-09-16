
from http import HTTPStatus
def test_end_to_end_bookstore_flow(client, creds):
    resp_user = client.create_user(creds.username, creds.password)
    assert resp_user.status_code in (HTTPStatus.OK, HTTPStatus.CREATED), resp_user.text
    user_id = resp_user.json().get("userID") or resp_user.json().get("userId")
    assert user_id, f"userID ausente: {resp_user.text}"
    resp_token = client.generate_token(creds.username, creds.password)
    assert resp_token.status_code == HTTPStatus.OK, resp_token.text
    token_json = resp_token.json()
    assert token_json.get("status") == "Success" and token_json.get("token"), token_json
    resp_auth = client.is_authorized(creds.username, creds.password)
    assert resp_auth.status_code == HTTPStatus.OK and resp_auth.json() is True, resp_auth.text
    resp_books = client.list_books()
    assert resp_books.status_code == HTTPStatus.OK, resp_books.text
    books = resp_books.json().get("books", [])
    assert len(books) >= 2, "Menos de dois livros disponíveis para seleção"
    isbns = [books[0]["isbn"], books[1]["isbn"]]
    resp_add = client.add_books_to_user(user_id, isbns)
    assert resp_add.status_code in (HTTPStatus.OK, HTTPStatus.CREATED), resp_add.text
    resp_get_user = client.get_user(user_id)
    assert resp_get_user.status_code == HTTPStatus.OK, resp_get_user.text
    user_books = resp_get_user.json().get("books", [])
    returned_isbns = sorted([b.get("isbn") for b in user_books])
    assert sorted(isbns) == returned_isbns, f"Esperado {isbns}, obtido {returned_isbns}"
