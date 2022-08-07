from firebase_admin import auth
from pkg.profile import profile as profile_module
from pkg.profile import basic_info as basic_info_module
from pkg.project import project as project_module
from pkg.file_module import file_module
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
