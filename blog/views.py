from urllib.parse import quote_plus
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
from django.http import HttpResponseRedirect, Http404
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.views.generic import DetailView

from .forms import PostForm
from .models import BlogPost


def post_list_view(request):
    list_objects = BlogPost.published.all()
    paginator = Paginator(list_objects, 3)
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    return render(request, 'blog/postlist.html', {'posts': posts})


def post_detail_view(request, year, month, day, post):
    post = get_object_or_404(BlogPost,
                             slug=post,
                             status='published',
                             publish__year=year,
                             publish__month=month,
                             publish__day=day)
    return render(request, 'blog/details.html', {'post': post})


# def post_create(request):
#     # user should can create post from this
#     # if not request.user.is_staff or not request.user.is_superuser:
#     #     raise Http404

#     form = PostForm(request.POST or None, request.FILES or None)
#     if form.is_valid():
#         instance = form.save(commit=False)
#         instance.user = request.user
#         instance.save()
#         # message success
#         messages.success(request, "Successfully Created")
#         return HttpResponseRedirect(instance.get_absolute_url())
#     context = {
#         "form": form,
#     }
#     return render(request, 'blog/post_form.html', context)


# Created for django code review
# class PostDetailView(DetailView):
#     template_name = "post_detail.html"

#     def get_object(self, *args, **kwargs):
#         slug = self.kwargs.get("slug")
#         instance = get_object_or_404(BlogPost, slug=slug)
#         if instance.publish > timezone.now().date() or instance.draft:
#             if not request.user.is_staff or not request.user.is_superuser:
#                 raise Http404
#         return instance

#     def get_context_data(self, *args, **kwargs):
#         context = super(PostDetailView, self).get_context_data(*args, **kwargs)
#         instance = context['object']
#         context['share_string'] = quote_plus(instance.content)
#         return context


# def post_detail(request, slug=None):
#     instance = get_object_or_404(BlogPost, slug=id)
#     if instance.publish > timezone.now().date() or instance.draft:
#         if not request.user.is_staff or not request.user.is_superuser:
#             raise Http404
#     share_string = quote_plus(instance.content)
#     context = {
#         "title": instance.title,
#         "instance": instance,
#         "share_string": share_string,
#     }
#     return render('blog/post_detail.html', context)


# def post_list(request):
#     today = timezone.now().date()
#     queryset_list = BlogPost.objects.active()
#     if request.user.is_staff or request.user.is_superuser:
#         queryset_list = BlogPost.objects.all()

#     query = request.GET.get("q")
#     if query:
#         queryset_list = queryset_list.filter(
#             # __icontains
#             # https://docs.djangoproject.com/en/2.0/topics/db/queries/#querysets-are-lazy
#             # https://stackoverflow.com/questions/2571149/what-is-this-mean-name-icontains-and-description-icontains-in-django-co
#             Q(title__icontains=query) |
#             Q(content__icontains=query) |
#             Q(user__first_name__icontains=query) |
#             Q(user__last_name__icontains=query)
#             ).distinct()
#     # show 8 contacts per page
#     paginator = Paginator(queryset_list, 8)
#     page_request_var = 'page'
#     page = request.GET.get(page_request_var)
#     try:
#         queryset = paginator.get_page(page)
#     except PageNotAnInteger:
#         # if page is not an integer, deliver first page.
#         queryset = paginator.get_page(1)
#     except EmptyPage:
#         # if page is out of range (e.g. 9999), deliver last page of results
#         queryset = paginator.get_page(paginator.num_pages)

#     context = {
#         "object_list": queryset,
#         "title": "List",
#         "page_request_var": page_request_var,
#         "today": today,
#     }
#     return render(request, 'blog/post_list.html', context)


# def post_update(request, slug=None):
#     if not request.user.is_staff or not request.user.is_superuser:
#         raise Http404
#     instance = get_object_or_404(BlogPost, slug=slug)
#     form = PostForm(request.POST or None,
#                     request.FILES or None,
#                     instance=instance)
#     if form.is_valid():
#         instance = form.save(commit=False)
#         instance.save()
#         messages.success(request,
#                          "<a href='#'>Item</a> Saved",
#                          extra_tags='html_safe')
#         return HttpResponseRedirect(instance.get_absolute_url())

#     context = {
#         "title": instance.title,
#         "instance": instance,
#         "form": form,
#     }
#     return render('blog/post_form.html', context)


# def post_delete(request, slug=None):
#     if not request.user.is_staff or not request.user.is_superuser:
#         raise Http404
#     instance = get_object_or_404(BlogPost, slug=slug)
#     instance.delete()
#     messages.success(redirect, "Successfully deleted")
#     return redirect("blog:list")



