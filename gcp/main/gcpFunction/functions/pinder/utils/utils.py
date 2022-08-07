import os
import tempfile


def get_env_count():
    os.environ["COUNT"] = str(int(os.environ.get("COUNT", "0")) + 1)
    return os.environ["COUNT"]


def get_tempfile_path(file_name):
    # file_name = secure_filename(filename)
    return os.path.join(tempfile.gettempdir(), file_name)
