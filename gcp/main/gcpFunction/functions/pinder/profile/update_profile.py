from loguru import logger
from pinder.utils.mongo_utils import get_db
from pinder.utils.utils import get_env_count
from pinder.utils.http_utils import http_err_msg_, http_success, http_success, http_unknown_error, http_uuid_not_provided


@logger.catch
def update_profile(request):
    try:
        db = get_db()

        request_data = request.get_json()
        logger.debug(get_env_count())
        logger.debug(request_data)
        if "uuid" not in request_data:
            return http_uuid_not_provided()

        key_name_list = [
            "name",
            "uuid",
            "roles",
            "seniority",
            "skills",
            "links",
            "location",
            "bio",
            "availability",
        ]

        if any([k not in key_name_list for k in request_data.keys()]):
            return http_err_msg_(f"arguments should be in the list: {key_name_list}"), 400

        rst = db["profile"].update_one({"uuid": request_data["uuid"]}, {"$set": request_data})
        if rst.matched_count == 0:
            return http_err_msg_("No user name matched"), 400
        return http_success()

    except Exception as e:
        logger.exception(e)
        return http_unknown_error()
