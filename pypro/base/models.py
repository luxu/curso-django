from django.db import models
from cloudinary.models import CloudinaryField


class Imagens(models.Model):
    description = models.CharField(max_length=100, null=True)
    image = models.ImageField(
        upload_to='images/',
        blank=True
    )
