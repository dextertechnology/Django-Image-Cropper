from django.db import models

class ImageCropperModel(models.Model):
    original_image = models.ImageField()
    edited_image = models.ImageField()

    def __str__(self):
        return self.original_image