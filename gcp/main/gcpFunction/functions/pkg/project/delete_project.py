from google.api_core import retry
from loguru import logger
from pkg.utils.mongo_utils import get_db
from pkg.project.validate import validate
from bson.objectid import ObjectId


@logger.catch
def delete_project(request):
    db = get_db()
    request_data = request.json
    logger.debug(request_data["_id"])

    """validate"""
    error = validate(db, request_data, "DELETE")
    if error:
        return {"error": error}, 400

    _id = request_data["_id"]

    if not db["project"].find({"_id": ObjectId(_id)}).count():
        return {"error": f"delete fail, project not found"}, 404

    rst = db["project"].delete_many({"_id": ObjectId(_id)})
    # return {'message': f"delete {rst.deleted_count} projects"}
    return {}
