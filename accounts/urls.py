from django.contrib.auth import views

from django.urls import path

from .views import account, register, view_profile, edit_profile, change_password
from django.contrib.auth.views import login, logout, password_reset, password_reset_done, password_reset_confirm, password_reset_complete

app_name = 'accounts'

urlpatterns = [
    path('', account, name='account'),
    path('login/', login, {'template_name': 'accounts/login.html'}, name='login'),
    path('logout/', logout, {'template_name': 'accounts/logout.html'}, name='logout'),
    path('register/', register, name='register'),
    path('profile/', view_profile , name='view_profile'),
    path('profile/edit/', edit_profile, name='edit_profile'),
    path('profile/password/', change_password, name='change_password'),
    
    # https://www.youtube.com/watch?v=cQET1DwWcwA&list=PLw02n0FEB3E3VSHjyYMcFadtQORvl1Ssj&index=31
    path('reset-password/', password_reset, {'template_name': 'accounts/reset_password.html', 'post_reset_redirect': 'accounts:password_reset_done', 'email_template_name': 'accounts/reset_password_email.html'}, name='reset_password'),

    path('reset-password/done/', password_reset_done, {'template_name': 'accounts/reset_password_done.html'}, name='password_reset_done'),

    path('reset-password/confirm/(?P<uidb64>[0-9A-Za-z]+)-(?P<token>,+)/', password_reset_confirm, {'template_name': 'accounts/reset_password_confirm.html', 'post_reset_redirect': 'accounts:password_reset_complete'}, name='password_reset_confirm'),
    
    path('reset-password/complete/', password_reset_complete, {'template_name': 'accounts/reset_password_complete.html'}, name='password_reset_complete')
]