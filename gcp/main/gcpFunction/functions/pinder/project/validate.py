def validate(db, request_data, method):
    if method == "POST" or method == "PUT":
        if "name" not in request_data or not request_data["name"]:
            return "name is required!"

        if request_data["name"] and not isinstance(request_data["name"], str):
            return "Wrong type of name, should be string!"

        # if  db['project'].find({"name": request_data["name"]}).count():
        #     return {'message': 'Duplicate project name found!'}

        if "roles" in request_data and (not isinstance(request_data["roles"], list) or any([not isinstance(role, str) for role in request_data["roles"]])):
            return "Wrong type of roles, should be string array!"

        if "category" in request_data and (not isinstance(request_data["category"], list) or any([not isinstance(c, str) for c in request_data["category"]])):
            return "Wrong type of category, should be string array!"

        if "stage" in request_data and (not isinstance(request_data["stage"], list) or any([not isinstance(s, str) for s in request_data["stage"]])):
            return "Wrong type of stage, should be string array!"

        if "image" in request_data["description"] and not isinstance(request_data["description"], str):
            return "Wrong type of description, should be string!"

        if "image" in request_data and not isinstance(request_data["image"], str):
            return "Wrong type of image, should be string!"

        if "location" in request_data and not isinstance(request_data["location"], str):
            return "Wrong type of location, should be string!"

        if "purpose" in request_data and not isinstance(request_data["purpose"], str):
            return "Wrong type of purpose, should be string!"

        if "rules" in request_data and not isinstance(request_data["rules"], str):
            return "Wrong type of rules, should be string!"

        if "hours" in request_data and not isinstance(request_data["hours"], str):
            return "Wrong type of hours, should be string!"
        """get, delete"""

    elif method == "GET":
        if "name" not in request_data or not request_data["name"]:
            return {"message": "name is required!"}
        if not isinstance(request_data["name"], str):
            return "Wrong type of name, should be string!"

    elif method == "DELETE":
        if "_id" not in request_data or not request_data["_id"]:
            return {"message": "_id is required!"}
        if not isinstance(request_data["_id"], str):
            return "Wrong type of _id, should be string!"

    return None
