from django.shortcuts import render,HttpResponse,redirect

# Create your views here.
def index(request):
    # return HttpResponse("Hello World")
    return render(request,'index.html')
def about(request):
    return render(request,"about.html")

def services(request):
    return render(request,"services.html")

def whyus(request):
    return