from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    username = None
    phone_number = models.CharField(max_length=10, unique=True)
    email = models.EmailField(unique=True)
    user_bio = models.CharField(max_length=50)
    user_profile_image = models.ImageField(upload_to='profileimages')

    USERNAME_FIELD = 'phone_number'
    REQUIRED_FIELDS = ['phone_number']