from loguru import logger

# import uuid
import os
from PIL import Image
from google.cloud import storage
from pinder.utils.utils import get_env_count, get_tempfile_path
from pinder.utils.http_utils import http_file_not_exist, http_image_file_format_err, http_unknown_error, http_uuid_not_provided, http_invalid_source_path
from pinder.utils.get_config import get_config

cfg = get_config()


@logger.catch
def insert_file(request):
    try:
        request_data = request.form.to_dict()
        logger.debug(get_env_count())
        logger.debug(request_data)
        if "uuid" not in request_data:
            return http_uuid_not_provided()

        source = request_data.get("source")
        if source not in ["project", "profile"]:
            return http_invalid_source_path()

        storage_client = storage.Client()
        # bucket_name = os.environ.get('pinder-image')
        bucket = storage_client.get_bucket(cfg.BUCKET_IMAGE_PATH)
        # TODO: limit file size
        img_file = request.files.get("file", None)
        if img_file is None:
            return http_file_not_exist()

        file_extension = os.path.splitext(img_file.filename)[-1]
        if file_extension not in [".jpg", ".png"]:
            logger.debug("{} {}", img_file.filename, file_extension)
            return http_image_file_format_err()

        img = Image.open(img_file)
        img = img.resize((cfg.IMAGE_W, cfg.IMAGE_H), Image.LANCZOS)

        tmp_file_name = get_tempfile_path(request_data["uuid"] + file_extension)
        img.save(tmp_file_name)

        file_save_path = os.path.join(source, os.path.basename(tmp_file_name))
        blob = bucket.blob(file_save_path)
        blob.upload_from_filename(tmp_file_name)

        os.remove(tmp_file_name)
        return os.path.join(cfg.BUCKET_URL, cfg.BUCKET_IMAGE_PATH, file_save_path), 200

    except Exception as e:
        logger.exception(e)
        return http_unknown_error()
