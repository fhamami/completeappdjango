from django.contrib import admin
from .models import BlogPost


class BlogPostAdmin(admin.ModelAdmin):
    list_display = ("title", "slug", "author", "status", "created")
    list_filter = ("status", "created", "publish", "updated")
    search_fields = ("title", "author")
    prepopulated_fields = {'slug': ('title',)}
    raw_id_fields = ('author',)
    date_hierarchy = 'publish'
    ordering = ['status', 'publish']

    class Meta:
        model = BlogPost


admin.site.register(BlogPost, BlogPostAdmin)