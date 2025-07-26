from tortoise import Tortoise 
import os
from dotenv import load_dotenv

load_dotenv()

DB_URL = os.getenv("DATABASE_URL")

TORTOISE_ORM = {
    "connections": {
        "default": DB_URL,
    },
    "apps": {
        "models": {
            "models": ["db.models", "aerich.models"],  
            "default_connection": "default",
        },
    },
}