from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models
from django.contrib import admin
from taggit.managers import TaggableManager
#from load_from_audiosearch import all_shows

# Get show_name_choices
import passwords as p
import math as m
#from audiosearch import Client


# Create your models here.
class podcast_show(models.Model):
#    show_name_choices = (all_shows)
#    show_name = models.CharField(max_length=255, choices = show_name_choices)
    show_id = models.CharField(max_length=6, null=True)
    show_name = models.CharField(max_length=255)
    show_description = models.TextField()
    show_website = models.CharField(max_length=100)
    show_slug = models.SlugField(unique=True)
    # Set choices for show format in admin
    show_format_choices = (
        ('Audioplay', 'Audioplay'),
        ('Unscripted', 'Unscripted')
    )
    show_format = models.CharField(max_length=20, choices = show_format_choices)
    show_tags = TaggableManager(verbose_name = "Show Tags", blank = True)
    
    def __str__(self):
        return self.show_name

class podcast_post(models.Model):
    # Try to get show choices from API
    podcast_show_info = models.ForeignKey(podcast_show, null=True) 
    post_title = models.CharField(max_length=255)
    post_content = models.TextField()
    slug = models.SlugField(unique=True)
    user = models.ForeignKey(User, blank=True, null=True)
    tags = TaggableManager(verbose_name = "Post Tags", blank = True)
    last_modified = models.DateTimeField(auto_now=True)
    
#    def __str__(self):
#        return self.last_modified