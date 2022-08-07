from loguru import logger
from pinder.file_module.insert_file import insert_file
from flask import jsonify
from pinder.utils.http_utils import http_method_not_allow_js, http_unknown_error_js, http_result_msg_


@logger.catch
def file_module(request):
    try:
        logger.debug("request.method={}", request.method)
        if request.method == "POST":
            rst, code = insert_file(request)
            return http_result_msg_(rst) if "error" not in rst else rst, code
        # elif request.method == 'PUT':
        #     rst, code = update_file(request)
        #     return jsonify(rst), code
        # elif request.method == 'DELETE':
        #     rst, code = delete_file(request)
        #     return jsonify(rst), code

        return http_method_not_allow_js()

    except Exception as e:
        logger.exception(e)
        return http_unknown_error_js()
