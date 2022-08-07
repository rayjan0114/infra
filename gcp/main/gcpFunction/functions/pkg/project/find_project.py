from loguru import logger
from pkg.utils.mongo_utils import get_db
from pkg.utils.get_config import get_config
from pkg.project.validate import validate
from bson.objectid import ObjectId


db = get_db()
cfg = get_config()


@logger.catch
def find_project(request):
    request_data = request.args.to_dict()
    logger.debug(request_data)

    if "all" not in request_data or not request_data["all"]:
        return find_by_id(request_data)
    else:
        return find_all()


@logger.catch
def find_by_id(request_data):
    """validate"""
    if "_id" not in request_data or not request_data["_id"]:
        return {"message": "_id is required!"}
    if not isinstance(request_data["_id"], str):
        return "Wrong type of _id, should be string!"
    result = db["project"].find_one({"_id": ObjectId(request_data["_id"])})
    if result:
        result["_id"] = str(result["_id"])
        return {"result": {"basic_info": cfg.BASIC_INFO_DEFAULT, "project": result}}, 200
    return {"message": "project not found"}, 404


@logger.catch
def find_all():
    result = []
    for p in db["project"].find():
        # del p['_id']
        p["_id"] = str(p["_id"])
        result.append(p)
    return {"result": result}, 200


@logger.catch
def find_by_name(request_data):
    """validate"""
    error = validate(db, request_data, "GET")
    if error:
        return {"error": error}, 400

    if not isinstance(request_data["name"], str):
        return {"error": "Wrong type of name, should be string!"}, 400

    result = db["project"].find_one({"name": request_data["name"]})

    if result:
        # del result['_id']
        result["_id"] = str(result["_id"])
        return {"result": result}, 200
    return {"error": "project not found"}, 404
