from django.contrib import admin
from .models import Home

class HomepageAdmin(admin.ModelAdmin):
	pass

admin.site.register(Home, HomepageAdmin)