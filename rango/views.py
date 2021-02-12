# from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def index(request):
    return HttpResponse("Hey there ! I am Muhammad Khalid"
                        + "<br> <a href='/rango/about/'>Go to About</a>")

def about(request):
    return HttpResponse("This is about page."
                        +"<br> <a href='/rango/'>Back to Index</a>")
