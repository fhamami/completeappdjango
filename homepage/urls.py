from django.urls import path
from .views import home

urlpatterns = [
    path('', home, name='homepage'),
    # path('', login_redirect, name='login_redirect')
]