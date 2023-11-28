from django.contrib import admin
from django.urls import path
from Index import views

urlpatterns = [
    path("",views.home,name="Home"),
]
