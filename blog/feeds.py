from django.contrib.syndication.views import Feed
from django.template.defaultfilters import truncatewords
from .models import BlogPost


class BlogPostFeed(Feed):
    title = 'Complete App Blog Feeds'
    link = '/blog/'
    description = 'Our latest Posts!'

    def items(self):
        return BlogPost.published.all()[:5]

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return truncatewords(item.body, 20)
