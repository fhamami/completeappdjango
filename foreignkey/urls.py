from django.conf.urls import url
from django.contrib.auth import views

from django.urls import path

from .views import items, categories


urlpatterns = [
    # url(r'^login/$', views.user_login, name='login'),
    path('item/', items, name='itemsFK'),
    path('category/', categories),
]