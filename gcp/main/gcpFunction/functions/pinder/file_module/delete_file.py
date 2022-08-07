from loguru import logger

from pinder.utils.http_utils import http_err_msg_, http_method_not_allow, http_success, http_success, http_unknown_error, http_uuid_not_provided


@logger.catch
def delete_file(request):
    try:
        if request.method != "DELETE":
            return http_method_not_allow()

        request_data = request.form.to_dict()
        logger.debug(request_data)
        if "uuid" not in request_data:
            return http_uuid_not_provided()

        if request_data["uuid"] == "TODO666":  # TODO: remove
            logger.warning("TODO666")  # TODO: remove
            request_data = {}  # TODO: remove

        # if rst.deleted_count != 1:
        #     return http_err_msg_("Delete {} profiles which is not 1.".format(rst.deleted_count)), 400
        return http_success()

    except Exception as e:
        logger.exception(e)
        return http_unknown_error()
