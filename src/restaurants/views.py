import random

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.views import View
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView

from .forms import RestaurantCreateForm, RestaurantLocationCreateForm
from .models import RestaurantLocation

class RestaurantListView(ListView):

    def get_queryset(self):
        #kwarg gets the user input from the url, it is called a slug
        return RestaurantLocation.objects.filter(owner=self.request.user)


class RestaurantDetailView(LoginRequiredMixin, DetailView):

    # Note: The available objects would be based on the queryset
    # Therefore if there is prefilter, the filtered query would be used
    def get_queryset(self):
        #kwarg gets the user input from the url, it is called a slug
        return RestaurantLocation.objects.filter(owner=self.request.user)

    # def get_object(self, *args, **kwargs):
    #     rest_id = self.kwargs.get('rest_id') #Ties the user keyword input (kwargs) to the variable rest_id
    #     obj = get_object_or_404(RestaurantLocation, id=rest_id) # Return obj where (object's pk = rest_id)
    #     return obj


class RestaurantCreateView(LoginRequiredMixin, CreateView):
    form_class = RestaurantLocationCreateForm
    template_name = "form.html"
    login_url = '/login/' # overwrites default login 
    success_url = "/restaurants/"

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.owner = self.request.user
        return super(RestaurantCreateView, self).form_valid(form)

    def get_context_data(self, *args, ** kwargs):
        context = super(RestaurantCreateView, self).get_context_data(*args, **kwargs)
        context['title'] = 'Add Restaurant'
        return context

class RestaurantUpdateView(LoginRequiredMixin, UpdateView):
    form_class = RestaurantLocationCreateForm
    template_name = "restaurants/detail-update.html"
    login_url = '/login/' # overwrites default login 

    def get_context_data(self, *args, ** kwargs):
        name = self.get_object().name
        context = super(RestaurantUpdateView, self).get_context_data(*args, **kwargs)
        context['title'] = f'Update Restaurant: {name}'
        return context

    def get_queryset(self):
        return RestaurantLocation.objects.filter(owner=self.request.user)