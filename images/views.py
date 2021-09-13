from rest_framework import viewsets
from rest_framework.permissions import AllowAny

from images import serializers
from images.models import Image


class ImageViewSet(viewsets.ModelViewSet):
    permission_classes = (AllowAny,)
    queryset = Image.objects.all()
    serializer_class = serializers.ImageSerializer
