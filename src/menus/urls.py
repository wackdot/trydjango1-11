from django.conf.urls import url

from .views import (
    ItemCreateView,
    ItemDetailView,
    ItemListView,
    ItemUpdateView
)

urlpatterns = [
    url(r'^create/$', ItemCreateView.as_view(), name='create'),
    # url(r'(?P<pk>\d+)/update/$', ItemUpdateView.as_view(), name='update'),
    url(r'(?P<pk>\d+)/$', ItemUpdateView.as_view(), name='details'),
    url(r'$', ItemListView.as_view(), name='list'),

]