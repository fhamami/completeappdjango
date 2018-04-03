# import re
from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.models import User


def upload_location(instance, filename):
    PostModel = instance.__class__
    new_id = PostModel.objects.order_by("id").last().id + 1

    return "%s/%s" % (new_id, filename)


class PublishedManager(models.Manager):
    def get_queryset(self):
        return super(PublishedManager,
                     self).get_queryset().filter(status='published')


class BlogPost(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published')
    )
    title = models.CharField(max_length=250)
    slug = models.SlugField(unique=True, unique_for_date='publish')
    author = models.ForeignKey(User,
                               on_delete=models.CASCADE,
                               related_name='blog_posts')
    body = models.TextField()
    draft = models.BooleanField(default=False)
    publish = models.DateField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10,
                              choices=STATUS_CHOICES,
                              default='draft')
    image = models.ImageField(upload_to=upload_location,
                              null=True,
                              blank=True,
                              width_field="width_field",
                              height_field="height_field")
    tags = models.CharField(max_length=50)

    objects = models.Manager()

    published = PublishedManager()

    class Meta:
        ordering = ['-publish', ]

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:post_detail_view',
                       args=[self.publish.year,
                             self.publish.strftime('%m'),
                             self.publish.strftime('%d'),
                             self.slug])
