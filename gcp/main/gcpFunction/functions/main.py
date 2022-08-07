from firebase_admin import auth
from pinder.profile import profile as profile_module
from pinder.profile import basic_info as basic_info_module
from pinder.project import project as project_module
from pinder.file_module import file_module
from loguru import logger


@logger.catch
def profile(request):
    return profile_module(request)


@logger.catch
def basicInfo(request):
    return basic_info_module(request)


@logger.catch
def project(request):
    return project_module(request)


@logger.catch
def fileApi(request):
    return file_module(request)
