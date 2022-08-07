from loguru import logger
from pinder.utils.mongo_utils import get_db
from pinder.utils.http_utils import http_err_msg_, http_unknown_error, http_uuid_not_exist, http_uuid_not_provided


@logger.catch
def find_profile(request):

    try:
        db = get_db()

        request_data = request.args.to_dict()
        logger.debug(request_data)

        if "uuid" not in request_data:
            return http_uuid_not_provided()

        if not isinstance(request_data["uuid"], str):
            return http_err_msg_("Wrong type of uuid, should be string!"), 400

        for doc in db["profile"].find({"uuid": request_data["uuid"]}):
            del doc["_id"]
            return doc, 200

        return http_uuid_not_exist()

    except Exception as e:
        logger.exception(e)
        return http_unknown_error()
