from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models
from django.contrib import admin
from taggit.managers import TaggableManager

# Create your models here.

class podcast_show(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    slug = models.SlugField(unique=True)
    user = models.ForeignKey(User, blank=True, null=True)
    tags = TaggableManager(verbose_name = "Tags", blank = True)
    
