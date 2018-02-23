from django.conf.urls import url
from django.contrib.auth import views

from django.urls import re_path

from blog.views import singlepost, yearview, monthview, tagview

urlpatterns = [
    # url(r'^login/$', views.user_login, name='login'),
    # url(r'^$', items, name='itemsFK'),
    re_path(r'^blog/<slug:title>', singlepost, name='singlepost'),
    # re_path(r'^blog/(\d{4,4})/(\d{2,2})/([\w\-]+)/$', singlepost, name='singlepost'),
    url(r'^blog/(\d{4,4})/$', yearview, name='yearview'),
    url(r'^blog/(\d{4,4})/(\d{2,2})/$', monthview, name='monthview'),
    url(r'^blog/tag/([\w\-]+)/$', tagview, name='tagview'),
]