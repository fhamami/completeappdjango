# from django.conf.urls import url
# from django.contrib.auth import views
from django.urls import path, include
from blog.views import (
    # post_list,
    # post_create,
    # post_detail,
    # post_update,
    # post_delete,
    # PostDetailView,
    post_list_view,
    post_detail_view
)
from .feeds import BlogPostFeed
# singlepost, yearview, monthview, tagview, frontpage

app_name = 'blog'

urlpatterns = [
    path('', post_list_view, name='post_list_view'),
    path('(<year>\d{4})/(<month>\d{2})/(<day>\d{2})/(<post>[-\w]+)/',
         post_detail_view, name='post_detail_view'),
    path('feed/', BlogPostFeed(), name='post_feed'),
    # path('foreignkey/', include('foreignkey.urls')),
    # path('create/', post_create, name='createpost'),
    # Django Code Review #3 on joincfe.com/youtube/
    # path('(<slug>[\w-]+)/', PostDetailView.as_view(), name='detail'),
    # path('(<slug>[\w-]+)/edit/', post_update, name='update'),
    # path('(<slug>)[\w-]+)/delete/', post_delete),
    # re_path(r'^blog/(\d{4,4})/(\d{2,2})/([\w\-]+)/$',
    #         singlepost,
    #         name='singlepost'),
    # path('blog/(\d{4,4})/', yearview, name='yearview'),
    # path('blog/(\d{4,4})/(\d{2,2})/', monthview, name='monthview'),
    # path('blog/tag/([\w\-]+)/', tagview, name='tagview'),
]
