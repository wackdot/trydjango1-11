import random

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.views import View
from django.views.generic import TemplateView, ListView, DetailView, CreateView

from .forms import RestaurantCreateForm, RestaurantLocationCreateForm
from .models import RestaurantLocation

@login_required(login_url='/login/')
def restaurant_createview(request):

    form = RestaurantLocationCreateForm(request.POST or None)
    errors = None

    if form.is_valid():
        if request.user.is_authenticated():
            instance = form.save(commit=False)
            # customisation
            # like a pre_save
            instance.owner = request.user
            instance.save()
            # like a post_save
            return HttpResponseRedirect("/restaurants/")
        else:
            return HttpResponseRedirect("/login/")
    
    if form.errors:
        errors = form.errors
    
    template_name = 'restaurants/form.html'
    context = {"form": form, "errors":errors}
    return render(request, template_name, context)

def restaurant_listview(request):

    template_name = 'restaurants/restaurants_list.html'

    queryset = RestaurantLocation.objects.all()

    context = {
        "object_list": queryset
    }
    return render(request, template_name, context)


class RestaurantListView(ListView):

    def get_queryset(self):
        #kwarg gets the user input from the url, it is called a slug
        slug = self.kwargs.get("slug") 
        if slug:
            queryset = RestaurantLocation.objects.filter(
                Q(category__iexact=slug) |
                Q(category__icontains=slug)
            )
        else:
            queryset = RestaurantLocation.objects.all()
        return queryset


class RestaurantDetailView(DetailView):

    # Note: The available objects would be based on the queryset
    # Therefore if there is prefilter, the filtered query would be used
    queryset = RestaurantLocation.objects.all()

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