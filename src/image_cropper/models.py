from django.db import models

class ImageCropperModel(models.Model):
    original_image = models.ImageField(upload_to="image/orginal")
    edited_image = models.ImageField(upload_to="image/cropped", null=True, blank=True)

    def __str__(self):
        return self.original_image.name