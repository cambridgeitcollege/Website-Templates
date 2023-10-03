from django.db import models

# Create your models here.
class ContactForm(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    
    class Meta:
        verbose_name = "Contact Form"
        verbose_name_plural = "Contact Forms"
