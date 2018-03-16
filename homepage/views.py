# from django.views.generic import TemplateView
from django.shortcuts import render, redirect
from django.contrib.auth.models import User

from .models import Home, Post, Friend
from .forms import HomeForm


def HomeView(request):
    template_name = 'homepage/homeform.html'

    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = HomeForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            post = form.save(commit=False)
            post.user = request.user
            post.save()

            text = form.cleaned_data['post']
            form = HomeForm()
            args = {'form': form, 'text': text}
            return render(request, template_name, args)

    # if a GET (or any other method) we'll create a blank form
    else:
        form = HomeForm()
        posts = Post.objects.all().order_by('-created')
        users = User.objects.exclude(id=request.user.id)
        friend = Friend.objects.get(current_user=request.user)
        friends = friend.users.all()
    
        args = {
            'form': form,
            'posts': posts,
            'users': users,
            'friends': friends
        }

        return render(request, template_name, args)


def Linklist(request):
    linklist = Home.objects.all()
    users = User.objects.exclude(id=request.user.id)

    context = {
        'linklist': linklist,
        'users': users,
    }

    return render(request, 'homepage/linklist.html', context)


def change_friends(request, operation, pk):
    friend = User.objects.get(pk=pk)
    if operation == 'add':
        Friend.make_friend(request.user, friend)
    elif operation == 'remove':
        Friend.lose_friend(request.user, friend)
    return redirect('homepage:home')
