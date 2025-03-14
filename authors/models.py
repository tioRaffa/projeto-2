from django.db import models
from django.contrib.auth import get_user_model
# Create your models here.

User = get_user_model()
class ProfileModels(models.Model):
    person = models.OneToOneField(User, verbose_name=("Person"), on_delete=models.CASCADE)
    bio = models.TextField(("Bio"), default='', blank=True)