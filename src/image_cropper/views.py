from django.shortcuts import render


def crop_image_view(request):
    return render(request, 'django_image_cropper/index.html')