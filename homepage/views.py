from django.shortcuts import render

from .models import Home

def home(request):
    context = {
        'linklist': Home.objects.all()
    }
    return render(request, 'homepage/linklist.html', context)