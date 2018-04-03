from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, get_object_or_404

from .models import BlogPost


def post_list_view(request):
    list_objects = BlogPost.published.all()
    paginator = Paginator(list_objects, 3)
    page = request.GET.get('page')
    try:
        posts = paginator.get_page(page)
    except PageNotAnInteger:
        posts = paginator.get_page(1)
    except EmptyPage:
        posts = paginator.get_page(paginator.num_pages)
    return render(request, 'blog/postlist.html', {'posts': posts})


def post_detail_view(request, year, month, day, post):
    post = get_object_or_404(BlogPost,
                             slug=post,
                             status='published',
                             publish__year=year,
                             publish__month=month,
                             publish__day=day)
    return render(request, 'blog/details.html', {'post': post})
