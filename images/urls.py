from django.urls import path, include
from rest_framework import routers

from images import views

app_name = 'images'
router = routers.DefaultRouter()
router.register('images', views.ImageViewSet, basename='images')

urlpatterns = [
    path('', include(router.urls)),
]
