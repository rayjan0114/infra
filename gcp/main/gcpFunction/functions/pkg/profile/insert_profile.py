from loguru import logger

# import uuid
from pkg.utils.mongo_utils import get_db
from pkg.utils.utils import get_env_count
from pkg.utils.http_utils import http_err_msg_, http_success, http_success, http_unknown_error, http_uuid_not_provided


@logger.catch
def insert_profile(request):
    try:
        db = get_db()

        request_data = request.get_json()
        logger.debug(get_env_count())
        logger.debug(request_data)
        if "uuid" not in request_data:
            return http_uuid_not_provided()

        if db["profile"].find({"uuid": request_data["uuid"]}).count():
            return http_err_msg_("Duplicate uuid found!"), 400

        data = {
            "name": "",
            "uuid": "",
            "roles": [],
            "seniority": "",
            "skills": [],
            "links": {
                "LinkedIn": "",
                "Behance": "",
                "Dribble": "",
                "Portfolio": "",
                "Resume": "",
                "Others": [],
            },
            "location": "",
            "bio": "",
            "availability": "",
        }
        for k, v in request_data.items():
            if k in data:
                data[k] = request_data[k]
        db["profile"].insert_one(data)
        return http_success(201)

    except Exception as e:
        logger.exception(e)
        return http_unknown_error()
