import re
from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=100)
    date_created = models.DateTimeField()
    date_modified = models.DateTimeField(auto_now=True)
    tags = models.CharField(max_length=200)
    body = models.TextField()

    def get_tag_list(self):
        return re.split(" ", self.tags)

    def __unicode__(self):
        return self.title

    def __str__(self):
        return self.title

    class Meta:
        ordering = ["-date_created"]

    class Admin:
        pass