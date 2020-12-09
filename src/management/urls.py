from django.conf.urls import url
from management import views


#Define the URLS to views routing 

urlpatterns = [
    #Define urls for Catalogue Operations
    url(r'^api/catalogues$', views.catalogue_list),
    url(r'^api/catalogues/(?P<pk>[0-9]+)$', views.catalogue_detail)
]
