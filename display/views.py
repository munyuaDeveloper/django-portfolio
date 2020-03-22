# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render


# Create your views here.
from .models import AboutMe


def HomePage(request):
    about = AboutMe.objects.all()
    context = {
        'aboutMe': about
    }
    return render(request, 'index.html', context)
