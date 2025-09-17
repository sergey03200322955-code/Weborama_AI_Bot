from dotenv import load_dotenv
import os

load_dotenv()

class Settings:
    TG_BOT_TOKEN = os.getenv("TG_BOT_TOKEN")
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
    DB_URL = os.getenv("DB_URL", "sqlite:///history.db")

settings = Settings()
