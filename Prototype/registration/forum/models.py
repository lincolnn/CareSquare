from django.db import models
from django.contrib.auth.models import User
from django.contrib import admin    
from string import join
from settings import MEDIA_ROOT

class Form(models.Model):
    title = models.CharField(max_length=60)
    def __unicode__(self):
        return self.title

class Thread(models.Model):
    title = models.CharField(max_length=60)
    created = models.DateTimeField(auto_now_add=True)
    creator = models.ForeignKey(User, blank=True, null=True)
    forum = models.ForeignKey(Forum)

    def __unicode__(self):
        return unicode(self.creator) + " - " + self.title

class Post(models.Model):
    title = models.CharField(max_length=60)
