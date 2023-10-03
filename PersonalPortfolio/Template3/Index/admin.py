from django.contrib import admin
from .models import *


# Register your models here.
class ContactUsDisplay(admin.ModelAdmin):
    list_display = ('id','name', 'email', 'message',"datetime")

#registering the model
admin.site.register(ContactForm, ContactUsDisplay)
