from django.shortcuts import render,HttpResponse

# Create your views here.
def home(reuest):
    # return HttpResponse("Hello World")
    return render(reuest,"index.html")