from django.db import models
from django.utils.text import slugify
from django.contrib.contenttypes.models import ContentType
# Create your models here.

class Tag(models.Model):
    name = models.CharField(_("Name"), max_length=250)
    slug = models.SlugField(_("Slug"), unique=True)
    
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.CharField(_("Object_Id"), max_length=50)
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = f'{slugify(self.name)}'
            
        return super().save(*args, **kwargs)