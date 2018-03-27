from django.db import models
from django.contrib.auth.models import User


STATUS_APP = (
    (0, 'On-Going'),
    (1, 'Finish'),
)


# app name
class Home(models.Model):
    class Meta:
        verbose_name_plural = 'App Name'

    url = models.CharField(max_length=50)
    title = models.CharField(max_length=200)
    date_start = models.DateTimeField(auto_now=True)
    date_end = models.DateTimeField(blank=True, null=True)
    status_app = models.SmallIntegerField(choices=STATUS_APP)

    def __str__(self):
        return self.title

# app wiki
# class WikiApp(models.Model):
#     class Meta:
#         verbose_name_plural = 'App Wiki'

# https://www.youtube.com/watch?v=qwE9TFNub84&list=PLw02n0FEB3E3VSHjyYMcFadtQORvl1Ssj&index=47


class Post(models.Model):
    post = models.CharField(max_length=500)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.post


class Friend(models.Model):
    users = models.ManyToManyField(User)
    current_user = models.ForeignKey(User, related_name='owner',
                                     null=True, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.current_user)

    # make friend methods
    @classmethod
    def make_friend(cls, current_user, new_friend):
        friend, created = cls.objects.get_or_create(
            current_user=current_user
        )
        friend.users.add(new_friend)

    @classmethod
    def lose_friend(cls, current_user, new_friend):
        friend, created = cls.objects.get_or_create(
            current_user=current_user
        )
        friend.users.remove(new_friend)
