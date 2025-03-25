from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index_page,name="index"),
    path('contact',views.contact_page,name="contact"),
    path('about',views.about_page,name="about"),
]
