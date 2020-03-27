# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from display.models import AboutMe, Services, Testimonial, Category, Project, ProjectImages,CustomersLogos

admin.site.register(AboutMe)
admin.site.register(Services)
admin.site.register(Testimonial)
admin.site.register(Category)
admin.site.register(Project)
admin.site.register(ProjectImages)
admin.site.register(CustomersLogos)