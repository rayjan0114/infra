from flask import jsonify


def http_err_msg_(msg):
    return {
        "error": {
            "message": msg,
        }
    }


def http_result_msg_(rst):
    return {
        "result": rst,
    }


# def http_add_ok_msg_(rst):
#     rst["message"] = "success"
#     return rst


def http_method_not_allow():
    return http_err_msg_("Method not allowed!"), 405


def http_uuid_not_provided():
    return http_err_msg_("uuid is not provided"), 400


def http_uuid_not_exist():
    return http_err_msg_("uuid doesn't exist"), 400


def http_file_not_exist():
    return http_err_msg_("File doesn't exist"), 400


def http_success(error_code=200):
    return {}, error_code


def http_unknown_error():
    return http_err_msg_("Unknown error!"), 400


def http_unknown_error_js():
    rst, code = http_unknown_error()
    return jsonify(rst), code


def http_method_not_allow_js():
    rst, code = http_method_not_allow()
    return jsonify(rst), code


def http_image_file_format_err():
    return http_err_msg_("Image shoud end with jpg or png"), 400


def http_invalid_source_path():
    return http_err_msg_("Invalid source path"), 400
