from django_q.tasks import async_task
from rest_framework import serializers

from images import models
from images.tasks import transform_image_task


class ImageSerializer(serializers.ModelSerializer):

    def create(self, validated_data):
        instance = super().create(validated_data)
        async_task(transform_image_task, instance.id)
        # transform_image_task(instance.id)
        return instance

    class Meta:
        model = models.Image
        fields = ['id', 'source_file', 'transform_file']
        read_only = ['transform_file']
