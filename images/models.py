from django.db import models


class Image(models.Model):
    source_file = models.ImageField()
    transform_file = models.ImageField(null=True, default=None)

    class Meta:
        verbose_name = 'image'
        verbose_name_plural = 'images'
