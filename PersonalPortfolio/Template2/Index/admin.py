from django.contrib import admin
from .models import ContactForm 
# Register your models here.


class DisplayContactForm(admin.ModelAdmin):
    list_display=['id','name','email','message','date']
    
admin.site.register(ContactForm, DisplayContactForm)
