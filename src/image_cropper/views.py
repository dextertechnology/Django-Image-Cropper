from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from image_cropper.forms import ImageCropperForm

@csrf_exempt
def crop_image_view(request):
    form = ImageCropperForm()
    context = {
        'form': form
    }

    if request.method == 'POST':
        print("=========================")
        print(request.POST)
        print(request.FILES)
        print("=========================")
    
    return render(request, 'django_image_cropper/index.html', context)