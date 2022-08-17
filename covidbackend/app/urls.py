from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name="home"),
    path('about', about, name="about"),
    path('symptoms', symptoms, name="symptoms"),
    path('vaccines', vaccines, name="vaccines"),
    path('registration', registration, name="registration"),
    path('contact', contact, name="contact"),
]
