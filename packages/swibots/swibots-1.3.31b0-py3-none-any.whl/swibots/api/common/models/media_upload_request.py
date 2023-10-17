import mimetypes, os, asyncio
from io import BytesIO
from logging import getLogger
from swibots.utils.types import (
    IOClient,
    ReadCallbackStream,
    UploadProgress,
    UploadProgressCallback,
)
from swibots.config import APP_CONFIG

from b2sdk.v2 import B2Api

logger = getLogger(__name__)

backblaze = B2Api()
bucket = None
if (account_id := APP_CONFIG["BACKBLAZE"].get("ACCOUNT_ID")) and (
    application_key := APP_CONFIG["BACKBLAZE"].get("APPLICATION_KEY")
):
    backblaze.authorize_account("production", account_id, application_key)
if (
    bucket_id := APP_CONFIG["BACKBLAZE"].get("BUCKET_ID")
) and backblaze.get_account_id():
    bucket = backblaze.get_bucket_by_id(bucket_id)


class MediaUploadRequest:
    def __init__(
        self,
        path: str | BytesIO,
        file_name: str = None,
        mime_type: str = None,
        caption: str = None,
        description: str = None,
        block: bool = True,
        callback: UploadProgressCallback = None,
        thumbnail: str = None,
        upload_args: tuple = (),
        reduce_thumbnail: bool = True,
        loop = None
    ):
        self.path = path
        self.file_name = file_name
        self.mime_type = mime_type
        self.caption = caption
        self.description = description
        self.block = block
        self.thumbnail = thumbnail
        self.callback = callback
        self.upload_args = upload_args
        self._handle_thumb = reduce_thumbnail
        self.loop = loop

    def get_media(self):
        if not self.mime_type:
            self.mime_type = (
                mimetypes.guess_type(self.file_name or self.path)[0]
                or "application/octet-stream"
            )
        file_response = bucket.upload_local_file(
            
            self.path,
            file_name=self.file_name or os.path.basename(self.path),
            content_type=self.mime_type,
            progress_listener=UploadProgress(
                self.path,
                callback=self.callback,
                callback_args=self.upload_args,
                loop=self.loop
            )
            if self.callback
            else None,
        ).as_dict()

        url = backblaze.get_download_url_for_fileid(file_response["fileId"])

        return {
            "caption": self.caption,
            "description": self.description,
            "mimeType": self.mime_type,
            "fileSize": file_response["size"],
            "fileName": file_response["fileName"],
            "downloadUrl": url,
            "thumbnailUrl": (
                self.file_to_url(self.thumbnail) if self.thumbnail != self.path else url
            )
            or url,
            "sourceUri": file_response["fileId"],
            "checksum": file_response["contentSha1"],
        }

    def data_to_request(self):
        return {
            "uploadMediaRequest.caption": self.caption,
            "uploadMediaRequest.description": self.description,
        }

    def data_to_params_request(self):
        return {
            "caption": self.caption,
            "description": self.description,
            "mimeType": self.get_mime_type(),
            "fileSize": os.path.getsize(self.path)
            if os.path.exists(self.path)
            else None
            #            "thumbnail":self.thumbnail
        }

    def get_mime_type(self):
        path = self.path.name if isinstance(self.path, BytesIO) else self.path
        return (
            self.mime_type
            or mimetypes.guess_type(path)[0]
            or "application/octet-stream"
        )

    def generate_thumbnail(
        self, path, radius: int = 5, resize: bool = False, quality: int = 80
    ):
        if self._handle_thumb:
            try:
                from PIL import Image, ImageFilter

                img = Image.open(path)
                if resize:
                    img.thumbnail((img.width // 2, img.height // 2), Image.BILINEAR)
                img = img.filter(ImageFilter.GaussianBlur(radius))
                obj = BytesIO()
                obj.name = os.path.basename(path)
                img.save(obj, optimize=True, quality=quality)
                return obj
            except ImportError:
                logger.debug(
                    "Pillow is not installed, Install it to add blur filter to thumbnail!"
                )
        return open(path, "rb")

    def file_to_url(self, path, mime_type: str = None, *args, **kwargs) -> str:
        if path:
            file = bucket.upload_local_file(
                path, path, content_type=mime_type, *args, **kwargs
            ).as_dict()
            return backblaze.get_download_url_for_fileid(file["fileId"])

    def file_to_request(self, url):
        d_progress = UploadProgress(
            current=0,
            readed=0,
            file_name=self.file_name,
            client=IOClient(),
            url=url,
            callback=self.callback,
            callback_args=self.upload_args,
        )
        reader = ReadCallbackStream(self.path, d_progress.update)
        d_progress._readable_file = reader
        path = self.path.name if isinstance(self.path, BytesIO) else self.path
        mime = self.get_mime_type()
        result = {"uploadMediaRequest.file": (self.file_name or path, reader, mime)}
        if self.thumbnail:
            if os.path.exists(self.thumbnail):
                thumb = self.generate_thumbnail(self.thumbnail)
                result["uploadMediaRequest.thumbnail"] = (
                    self.thumbnail,
                    thumb,
                    mimetypes.guess_type(self.thumbnail)[0],
                )
            else:
                logger.error(
                    f"provided thumbnail: {self.thumbnail} is not a valid path!"
                )
        return d_progress, result
