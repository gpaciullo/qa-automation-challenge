
import secrets, string
import pytest
from src.models.credentials import Credentials

def _strong_password(length: int = 12) -> str:
    # garante ao menos 1 de cada categoria
    chars = [
        secrets.choice(string.ascii_lowercase),
        secrets.choice(string.ascii_uppercase),
        secrets.choice(string.digits),
        secrets.choice("!@#$%^&*()-_=+[]{}:;,.?/"),
    ]
    pool = string.ascii_letters + string.digits + "!@#$%^&*()-_=+[]{}:;,.?/"
    chars += [secrets.choice(pool) for _ in range(length - len(chars))]
    secrets.SystemRandom().shuffle(chars)
    return "".join(chars)

@pytest.fixture
def creds():
    username = f"qa_{secrets.token_hex(6)}"
    password = _strong_password(12)   # sempre atende aos requisitos
    return Credentials(username=username, password=password)