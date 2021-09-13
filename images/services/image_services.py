import io
import sys

from PIL import Image
from django.core.files import File
from django.core.files.uploadedfile import InMemoryUploadedFile


def rotate_uploaded_image(img_file: File) -> InMemoryUploadedFile:
    original_img = io.BytesIO(img_file.read())
    img = Image.open(original_img)
    im_rotate = img.rotate(180)
    thumb_io = io.BytesIO()

    im_rotate.save(thumb_io, format='JPEG')
    new_file = InMemoryUploadedFile(
        file=thumb_io,
        field_name=None,
        name=img_file.name,
        content_type='image/jpeg',
        size=sys.getsizeof(thumb_io),
        charset=None
    )
    return new_file
