from django.forms import ModelForm

from image_cropper.models import ImageCropperModel


class ImageCropperForm(ModelForm):
    class Meta:
        model = ImageCropperModel
        fields = ('original_image','edited_image',)