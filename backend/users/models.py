from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class ApplicationUser(AbstractUser):
    avatar = models.ImageField(blank=True)