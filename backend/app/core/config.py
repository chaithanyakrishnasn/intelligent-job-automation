from dotenv import load_dotenv
import os

load_dotenv()


class Settings:
    APP_NAME = "Intelligent Job Automation System"
    DATABASE_URL = os.getenv(
        "DATABASE_URL", "postgresql://user:password@localhost:5432/jobs")


settings = Settings()
