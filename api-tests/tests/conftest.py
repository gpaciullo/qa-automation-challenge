
import os, uuid, random, string, pytest
from src.client.api_client import DemoQAClient
from src.config import BASE_URL, Credentials
_DEF_PASSWORD = "Aa!" + "".join(random.choices(string.ascii_letters + string.digits, k=8))
@pytest.fixture(scope="session")
def creds() -> Credentials:
    username = os.getenv("DEMOQA_USERNAME") or f"qa_{uuid.uuid4().hex[:10]}"
    password = os.getenv("DEMOQA_PASSWORD") or _DEF_PASSWORD
    return Credentials(username=username, password=password)
@pytest.fixture(scope="session")
def client() -> DemoQAClient:
    return DemoQAClient(BASE_URL)
