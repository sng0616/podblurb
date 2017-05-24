# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-05-15 07:18
from __future__ import unicode_literals

from django.db import migrations
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        ('taggit', '0002_auto_20150616_2121'),
        ('collection', '0004_podcast_show_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='podcast_post',
            name='tags',
            field=taggit.managers.TaggableManager(help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags'),
        ),
    ]
