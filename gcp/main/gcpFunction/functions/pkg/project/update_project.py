from loguru import logger
from pkg.utils.mongo_utils import get_db
from pkg.project.validate import validate
from bson.objectid import ObjectId


db = get_db()


@logger.catch
def update_project(request):
    request_data = request.json
    logger.debug(request_data)

    """validate"""
    error = validate(db, request_data, "PUT")
    if error:
        return {"error": error}, 400

    key_name_list = ["_id", "name", "roles", "description", "image", "stage", "location", "category", "purpose", "rules", "hours"]

    if any([k not in key_name_list for k in request_data.keys()]):
        return f"arguments should be in the list: {key_name_list}", 400

    rst = db["project"].update_one({"_id": ObjectId(request.args["_id"])}, {"$set": request_data})
    if rst.matched_count == 0:
        return {"error": "project not found"}, 404
    print(rst.raw_result)
    return {}
