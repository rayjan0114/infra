import os
from dotenv import load_dotenv

from google.cloud import secretmanager
import pymongo
from loguru import logger

load_dotenv()


@logger.catch
def get_db():
    if not os.getenv("DEBUG"):
        project_id = os.environ["GCP_PROJECT"]
        client = secretmanager.SecretManagerServiceClient()
        name = f"projects/{project_id}/secrets/mongo-password/versions/latest"
        response = client.access_secret_version(name=name)
        password = response.payload.data.decode("UTF-8")
    else:
        password = os.getenv("MONGODB_PASSWORD")
    client = pymongo.MongoClient(f"mongodb+srv://pinder001:{password}@cluster0.y7btn.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
    db = client.data
    return db
