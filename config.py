import os
from dotenv import load_dotenv

# LOAD .env FILE
load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
QDRANT_URL = os.getenv("QDRANT_URL")
COLLECTION_NAME = "book_chapters"