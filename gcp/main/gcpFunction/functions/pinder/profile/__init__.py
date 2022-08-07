from loguru import logger
from pinder.utils.get_config import get_config
from pinder.profile.delete_profile import delete_profile
from pinder.profile.insert_profile import insert_profile
from pinder.profile.find_profile import find_profile
from pinder.profile.update_profile import update_profile
from flask import jsonify
from pinder.utils.http_utils import http_method_not_allow_js, http_unknown_error_js, http_result_msg_

cfg = get_config()


@logger.catch
def profile(request):
    try:
        logger.debug("request.method={}", request.method)
        if request.method == "POST":
            rst, code = insert_profile(request)
            return jsonify(rst), code
        elif request.method == "GET":
            rst, code = find_profile(request)
            return http_result_msg_(rst) if "error" not in rst else rst, code
        elif request.method == "PUT":
            rst, code = update_profile(request)
            return jsonify(rst), code
        elif request.method == "DELETE":
            rst, code = delete_profile(request)
            return jsonify(rst), code

        return http_method_not_allow_js()

    except Exception as e:
        logger.exception(e)
        return http_unknown_error_js()


@logger.catch
def basic_info(request):
    try:
        if request.method == "GET":
            rst = {}
            rst["profile"], err_code = find_profile(request)
            rst["basicInfo"] = cfg.BASIC_INFO_DEFAULT
            return jsonify(rst), err_code

        return http_method_not_allow_js()

    except Exception as e:
        logger.exception(e)
        return http_unknown_error_js()
