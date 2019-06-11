from django import forms
from PIL import Image

from image_cropper.models import ImageCropperModel


class ImageCropperForm(forms.ModelForm):
    x = forms.FloatField(widget=forms.HiddenInput())
    y = forms.FloatField(widget=forms.HiddenInput())
    width = forms.FloatField(widget=forms.HiddenInput())
    height = forms.FloatField(widget=forms.HiddenInput())
    class Meta:
        model = ImageCropperModel
        fields = ('original_image','edited_image','x','y','width','height',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['original_image'].widget.attrs.update({
            'class': 'form-control-file',
            'required': True
        })
        
    def save(self):
        photo = super(ImageCropperForm, self).save()

        x = self.cleaned_data.get('x')
        y = self.cleaned_data.get('y')
        w = self.cleaned_data.get('width')
        h = self.cleaned_data.get('height')

        image = Image.open(photo.original_image)
        cropped_image = image.crop((x, y, w+x, h+y))
        cropped_image.save(photo.edited_image.path)
        return photo