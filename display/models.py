# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


# Create your models here.

class AboutMe(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    profile_img = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.title
