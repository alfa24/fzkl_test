from images import models
from images.services.image_services import rotate_uploaded_image


def transform_image_task(image_id: int):
    img = models.Image.objects.get(id=image_id)
    img.transform_file = rotate_uploaded_image(img.source_file.file)
    img.save()
