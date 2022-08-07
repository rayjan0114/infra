from loguru import logger
from pinder.utils.get_config import get_config
from pinder.project.find_project import find_project
from pinder.project.create_project import create_project
from pinder.project.update_project import update_project
from pinder.project.delete_project import delete_project


@logger.catch
def project(request):
    try:
        if request.method == "GET":
            return find_project(request)
        elif request.method == "POST":
            return create_project(request)
        elif request.method == "PUT":
            return update_project(request)
        elif request.method == "DELETE":
            return delete_project(request)

        return "Method not allowed!", 405

    except Exception as e:
        logger.error(e)
        return {"error": e}, 400
