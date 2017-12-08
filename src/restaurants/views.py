import random

from django.http import HttpResponse
from django.shortcuts import render
from django.views import View

# Create your views here.
# function based view
def home1(request):
    num = random.randint(0, 1000)

    if (num < 500):
        value = False
    else:
        value = True
    
    random_num_list = [
        random.randint(0, 1000), 
        random.randint(0, 1000), 
        random.randint(0, 1000)
        ]

    context = {
        "html_tag": "Testing123", 
        "bool": value, 
        "num": num,
        "random_num_list": random_num_list
        }

    return render(request, "home1.html", context) #response

def home2(request):
    num = random.randint(0, 1000)

    if (num < 500):
        value = False
    else:
        value = True
    
    random_num_list = [
        random.randint(0, 1000), 
        random.randint(0, 1000), 
        random.randint(0, 1000)
        ]

    context = {
        "html_tag": "Testing123", 
        "bool": value, 
        "num": num,
        "random_num_list": random_num_list
        }

    return render(request, "home2.html", context) #response


def home3(request):
    num = random.randint(0, 1000)

    if (num < 500):
        value = False
    else:
        value = True
    
    random_num_list = [
        random.randint(0, 1000), 
        random.randint(0, 1000), 
        random.randint(0, 1000)
        ]

    context = {
        "html_tag": "Testing123", 
        "bool": value, 
        "num": num,
        "random_num_list": random_num_list
        }

    return render(request, "home3.html", context) #response


def about(request):
    context = {}
    return render(request, "about.html", context) #response


def contact(request):
    context = {}
    return render(request, "contact.html", context) #response

def ContactView(View):
    def get(self, request, *args, **kwargs):
        return 