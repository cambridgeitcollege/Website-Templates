from django.shortcuts import render
from .models import *

# Create your views here.
def home(request):
    if(request.method=="POST"):
        name=request.POST.get("name")
        email=request.POST.get("email")
        message=request.POST.get("message")
        contact=ContactForm(name=name,email=email,message=message)
        try:
            contact.save()
        except:
            pass
        
            # return HttpResponse("Hello World")
    return render(request,"index.html")