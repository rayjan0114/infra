from loguru import logger
from pinder.utils.mongo_utils import get_db
from pinder.project.validate import validate


@logger.catch
def create_project(request):

    db = get_db()
    request_data = request.json

    logger.debug("request_data: ", request_data)

    """validate"""
    error = validate(db, request_data, "POST")
    if error:
        return {"error": error}, 400

    data = {
        "name": "",
        "roles": [],
        "description": "",
        "image": "",
        "stage": [],
        "location": "tw",
        "category": [],
        "purpose": "",
        "rules": "",
        "hours": "1 hours per week",
    }
    for k, v in request_data.items():
        if k in data:
            data[k] = v
    result = db["project"].insert_one(data)
    logger.debug(f"project: {result.inserted_id} create success")
    return {}, 201
