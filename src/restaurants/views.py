import random

from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from django.views.generic.base import TemplateView

# Create your views here.
# function based view
# def home1(request):
#     num = random.randint(0, 1000)

#     if (num < 500):
#         value = False
#     else:
#         value = True
    
#     random_num_list = [
#         random.randint(0, 1000), 
#         random.randint(0, 1000), 
#         random.randint(0, 1000)
#         ]

#     context = {
#         "html_tag": "Testing123", 
#         "bool": value, 
#         "num": num,
#         "random_num_list": random_num_list
#         }

#     return render(request, "home1.html", context) #response

# Class based view
class HomeView(TemplateView):
    template_name = "home.html"

    # Implementing existing class method
    def get_context_data(self, *args, **kwargs):

        context = super(HomeView, self).get_context_data(*args, **kwargs)
        
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

        return context
        