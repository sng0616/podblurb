from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models
from django.contrib import admin
from taggit.managers import TaggableManager

# Create your models here.
class podcast_show(models.Model):
    show_name = models.CharField(max_length=255)
    show_description = models.TextField()
    show_website = models.CharField(max_length=100)
    show_slug = models.SlugField(unique=True)
    # Set choices for show format in admin
    show_format_choices = (
        ('Scripted', 'Scripted'),
        ('Talk', 'Talk')
    )
    show_format = models.CharField(max_length=20, choices = show_format_choices)

class podcast_post(models.Model):
    # Try to get show choices from API
    podcast_show_info = models.ForeignKey(podcast_show, null=True) 
    post_title = models.CharField(max_length=255)
    post_content = models.TextField()
    slug = models.SlugField(unique=True)
    user = models.ForeignKey(User, blank=True, null=True)
    tags = TaggableManager(verbose_name = "Tags", blank = True)
    last_modified = models.DateField(auto_now=False,auto_now_add=False)