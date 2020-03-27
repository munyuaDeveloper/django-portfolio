# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render


# Create your views here.
from .models import AboutMe, Services, Testimonial, Project, Category, CustomersLogos


def HomePage(request):
    about = AboutMe.objects.all()
    services = Services.objects.all()[:3]
    testimonials = Testimonial.objects.all()
    projects = Project.objects.all()
    categories = Category.objects.all()
    customers_logos = CustomersLogos.objects.all()[:6]

    context = {
        'aboutMe': about,
        'services': services,
        'testimonials': testimonials,
        'projects': projects,
        'categories': categories,
        'customers_logos': customers_logos
    }
    return render(request, 'index.html', context)
