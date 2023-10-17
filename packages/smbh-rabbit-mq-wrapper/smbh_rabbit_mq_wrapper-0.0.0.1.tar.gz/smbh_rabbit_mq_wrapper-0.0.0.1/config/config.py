from pathlib import Path

from dotenv import load_dotenv

# Setup paths variables
PROJECT_PATH = Path(__file__).parent.resolve()


def load_config(path=f"{PROJECT_PATH}/.env"):
    load_dotenv(path)


load_config()
