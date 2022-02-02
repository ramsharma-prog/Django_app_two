from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from PIL import Image

from django_resized import ResizedImageField

# ACCOUNTS MODELS


class Profile(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, default="")
    # image = models.ImageField(default='default.jpeg', upload_to='profile_pics')
    image = ResizedImageField(
        size=[100, 100], crop=['middle', 'center'], upload_to='profile_pics', default='default.jpeg')

    def __str__(self):
        return f"{self.user.username} Profile"

    # ------ANOTHER WAY OF RESIZING THE IMAGE -----#

    # def save(self, *args, **kwargs):
    #     super(Profile, self).save(*args, **kwargs)
    #     img = Image.open(self.image.path)
    #     if img.height > 150 or img.width > 150:
    #         output_size = (150, 150)
    #         img.thumbnail(output_size)
    #         img.save(self.image.path)
