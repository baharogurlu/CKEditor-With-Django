from django.db import models


from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.
from django.forms import CharField


class Post(models.Model):
    content = models.CharField(max_length=1000, blank=True)
    description = models.CharField(max_length=1000, blank=True,null=True)
