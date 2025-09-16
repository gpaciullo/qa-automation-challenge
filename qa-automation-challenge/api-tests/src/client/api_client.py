
from __future__ import annotations
import requests
from typing import List
class DemoQAClient:
    def __init__(self, base_url: str) -> None:
        self.base_url = base_url.rstrip("/")
        self.session = requests.Session()
        self._token: str | None = None
    def create_user(self, username: str, password: str) -> requests.Response:
        return self.session.post(f"{self.base_url}/Account/v1/User", json={"userName": username, "password": password})
    def generate_token(self, username: str, password: str) -> requests.Response:
        resp = self.session.post(f"{self.base_url}/Account/v1/GenerateToken", json={"userName": username, "password": password})
        if resp.ok:
            token = resp.json().get("token")
            if token:
                self._token = token
                self.session.headers.update({"Authorization": f"Bearer {token}"})
        return resp
    def is_authorized(self, username: str, password: str) -> requests.Response:
        return self.session.post(f"{self.base_url}/Account/v1/Authorized", json={"userName": username, "password": password})
    def get_user(self, user_id: str) -> requests.Response:
        return self.session.get(f"{self.base_url}/Account/v1/User/{user_id}")
    def list_books(self) -> requests.Response:
        return self.session.get(f"{self.base_url}/BookStore/v1/Books")
    def add_books_to_user(self, user_id: str, isbns: List[str]) -> requests.Response:
        payload = {"userId": user_id, "collectionOfIsbns": [{"isbn": i} for i in isbns]}
        return self.session.post(f"{self.base_url}/BookStore/v1/Books", json=payload)
    def delete_all_books(self, user_id: str) -> requests.Response:
        return self.session.delete(f"{self.base_url}/BookStore/v1/Books?UserId={user_id}")
