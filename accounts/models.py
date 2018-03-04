from django.db import models
from django.contrib.auth.models import User

from django.db.models.signals import post_save

class UserProfile(models.Model):
    # what is OneToOneField? and why?
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    description = models.CharField(max_length=100, null=True, blank=True) # default it will be empty
    city = models.CharField(max_length=100, null=True, blank=True)
    website = models.URLField(null=True, blank=True)
    phone = models.IntegerField(default=0) # IntegerField can't leave with empty string, becauce type conflict
    image = models.ImageField(upload_to='profile_image', blank=True)

    def __str__(self):
        return self.user.username

# automaticly added new user to UserProfile when user created
def create_profile(sender, **kwargs):
    # if user object has been created
    if kwargs['created']:
        # kwargs['instance'] it will return user object and then pass the user object into UserProfile
        # it associtating the user that has been created with the UserProfile
        user_profile = UserProfile.objects.create(user=kwargs['instance'])

post_save.connect(create_profile, sender=User)