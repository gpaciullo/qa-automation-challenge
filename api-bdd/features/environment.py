
import os
import uuid
import random
import string
from dotenv import load_dotenv
import requests

def before_all(context):
    load_dotenv()
    context.base_url = os.getenv("DEMOQA_BASE_URL", "https://demoqa.com").rstrip("/")
    context.session = requests.Session()

    # Gera credenciais válidas por execução (atende política de senha)
    username = os.getenv("DEMOQA_USERNAME") or f"qa_{uuid.uuid4().hex[:10]}"
    rand_tail = "".join(random.choices(string.ascii_letters + string.digits, k=8))
    password = os.getenv("DEMOQA_PASSWORD") or f"Aa!{rand_tail}"
    context.creds = {"userName": username, "password": password}

    context.state = {}
