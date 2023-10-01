from django.shortcuts import render,redirect
from .models import ContactForm

# Create your views here.
def home(request):
    if request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        message=request.POST.get('message')
        data=ContactForm(name=name,email=email,message=message)
        try:
            data.save()
        except:
            pass
    return render(request, 'index.html')

