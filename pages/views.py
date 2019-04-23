from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def home_view(request, *args, **kwargs):
    
    print(request.user)
    print(args, kwargs)
    #return HttpResponse("<h1>Hello Woorld</h1>")

    context = {
        "home_active": "active"
    }

    return render (request, "home.html", context)

def products_view(request, *args, **kwargs):
    return HttpResponse("<h1>Product List</h1>")


def about_view(request, *args, **kwargs):
    print(request.user)
    print(args, kwargs)
    
    context = {
        "about_active": "active",
        "my_text": "This is my story: ",
        "my_number": 123,
        "my_list": [123, 321, 444],
        "my_condition": False,

    }

    return render (request, "about.html", context)


def contact_view(request, *args, **kwargs):
    print(request.user)
    print(args, kwargs)

    context = {
        "contact_active": "Active"
    }

    #return HttpResponse("<h1>Hello Woorld</h1>")
    return render (request, "contact.html", context)