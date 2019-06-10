import json

from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt

from image_cropper.forms import ImageCropperForm
from image_cropper.models import ImageCropperModel

def crop_image_view(request):
    form_class = ImageCropperForm()
    context = {
        'form': form_class,
        'objects': ImageCropperModel.objects.all()
    }

    if request.method == 'POST':
        form = ImageCropperForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('crop_image')
        else:
            print("Form is invalid")
    return render(request, 'django_image_cropper/index.html', context)