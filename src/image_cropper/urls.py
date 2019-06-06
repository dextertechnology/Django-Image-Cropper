from django.urls import path

from image_cropper.views import crop_image_view


urlpatterns = [
    path('', crop_image_view, name='crop_image')
]