from django.contrib import admin

from .models import Category, Item

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']

class ItemAdmin(admin.ModelAdmin):
    list_display = ['name']


admin.site.register(Category, CategoryAdmin)
admin.site.register(Item, ItemAdmin)
