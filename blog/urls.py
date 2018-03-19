from django.conf.urls import url
# from django.contrib.auth import views

from django.urls import re_path, path

from blog.views import singlepost, yearview, monthview, tagview, frontpage

urlpatterns = [
    path('', frontpage, name='frontpage'),
    re_path(r'^blog/<slug:title>', singlepost, name='singlepost'),
    re_path(r'^blog/(\d{4,4})/(\d{2,2})/([\w\-]+)/$',
            singlepost,
            name='singlepost'),
    path('blog/(\d{4,4})/', yearview, name='yearview'),
    path('blog/(\d{4,4})/(\d{2,2})/', monthview, name='monthview'),
    path('blog/tag/([\w\-]+)/', tagview, name='tagview'),
]