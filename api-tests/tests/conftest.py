
import secrets, string
import pytest
from src.models.credentials import Credentials  # ajuste o import conforme seu projeto

def _strong_password(length: int = 12) -> str:
    # garante 1 de cada categoria
    chars = [
        secrets.choice(string.ascii_lowercase),
        secrets.choice(string.ascii_uppercase),
        secrets.choice(string.digits),
        secrets.choice("!@#$%^&*()-_=+[]{}:;,.?/"),
    ]
    # completa o restante com um mix
    pool = string.ascii_letters + string.digits + "!@#$%^&*()-_=+[]{}:;,.?/"
    chars += [secrets.choice(pool) for _ in range(max(8, length) - len(chars))]
    # embaralha para não ficar previsível
    secrets.SystemRandom().shuffle(chars)
    return "".join(chars)

@pytest.fixture
def creds():
    username = f"qa_{secrets.token_hex(6)}"
    password = _strong_password(12)   # <- agora sempre cumpre a política
    return Credentials(username=username, password=password)
