# from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

from django.shortcuts import render


def index(request):
    context_dict = {'boldMessage': "Crunchy, creamy, cookie, candy, cupcake !"}
    return render(request, 'rango/index.html', context=context_dict)


def about(request):
    context_dict = {'myName': "Muhammad Khalid"}
    return render(request, 'rango/about.html', context=context_dict)
