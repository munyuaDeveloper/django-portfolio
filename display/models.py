# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models


# Create your models here.

class AboutMe(models.Model):
    title = models.CharField(max_length=200)
    description = RichTextUploadingField(blank=True,
                                         null=True,
                                         config_name='default')
    profile_img = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.title


class Services(models.Model):
    title = models.CharField(max_length=200)
    iconClass = models.CharField(max_length=50, default='fa fa-search')
    description = RichTextUploadingField(blank=True,
                                         null=True,
                                         config_name='default')

    def __str__(self):
        return self.title


class Testimonial(models.Model):
    user_message = RichTextUploadingField(blank=True,
                                          null=True,
                                          config_name='default')

    user_name = models.CharField(max_length=200)
    user_position = models.CharField(max_length=200)
    user_image = models.ImageField()

    def __str__(self):
        return self.user_name


class Category(models.Model):
    category = models.CharField(max_length=200)

    def __str__(self):
        return self.category


class ProjectImages(models.Model):
    image_alternative = models.CharField(max_length=50)
    image = models.ImageField()

    def __str__(self):
        return self.image_alternative


class Project(models.Model):
    project_title = models.CharField(max_length=200)
    project_short_desc = models.TextField()
    project_full_desc = RichTextUploadingField(blank=True,
                                               null=True,
                                               config_name='default')
    project_category = models.ForeignKey(Category, on_delete=models.CASCADE)
    project_profile_image = models.ImageField()
    Project_images = models.ManyToManyField(ProjectImages)

    def __str__(self):
        return self.project_title

class CustomersLogos(models.Model):
    company_name = models.CharField(max_length=200)
    company_logo = models.ImageField()

    def __str__(self):
        return self.company_name
