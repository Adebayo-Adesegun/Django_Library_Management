from django.conf.urls import url, include
from rest_framework import routers
from rest_framework import urlpatterns
from .views import UserViewSet

#The DefaultRouter class will define the standard REST (GET, POST, PUT, DELETE … ) endpoints for a resource
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)


urlpatterns = [
    url(r'^', include(router.urls)),
]