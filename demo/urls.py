from django.urls import path

from demo.views import index, gallery

app_name = 'demo'
urlpatterns = [
    path('', index, name='index'),
    path('gallery/', gallery, name='gallery'),
]
