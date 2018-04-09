from django.urls import path
from .views import HomeView, Linklist, change_friends

app_name = 'homepage'

urlpatterns = [
    path('userposts/', HomeView, name='userposts'),
    path('', Linklist, name='linklist_view'),
    path('connect/(<operation>.+)/(<int:pk>\d+)/', change_friends,
         name='change_friends')
]