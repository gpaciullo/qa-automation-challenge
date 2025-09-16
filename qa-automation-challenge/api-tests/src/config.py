
from dataclasses import dataclass
import os
from dotenv import load_dotenv
load_dotenv()
BASE_URL = os.getenv("DEMOQA_BASE_URL", "https://demoqa.com")
@dataclass
class Credentials:
    username: str | None = os.getenv("DEMOQA_USERNAME")
    password: str | None = os.getenv("DEMOQA_PASSWORD")
