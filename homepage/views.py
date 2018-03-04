from django.shortcuts import render, redirect

from .models import Home
from .forms import HomeForm

def home(request):

    # def get(self, request):
    #     form = HomeForm()

    context = {
        'linklist': Home.objects.all(),
        # 'form': HomeForm(),
    }

    return render(request, 'homepage/homepage.html', context)

def login_redirect(request):
    return redirect('accounts/login')