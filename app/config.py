import os
from dotenv import load_dotenv

load_dotenv()

GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
AI_API_KEY = os.getenv("AI_API_KEY")
