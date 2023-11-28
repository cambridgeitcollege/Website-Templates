from django.shortcuts import render,HttpResponse,redirect

# Create your views here.
def index(request):
    # return HttpResponse("Hello World")
    return render(request,'index.html')
def about(request):
    return render(request,"about.html")

def services(request):
    return render(request,"service.html")

def whyus(request):
    return render(request,"why.html")

def team(request):
    return render(request,"team.html")

def base(request):
    return render(request,'base.html')