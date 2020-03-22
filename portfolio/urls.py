from django.contrib import admin
from django.urls import path
from display import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.HomePage),
]
