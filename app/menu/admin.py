from django.contrib import admin

from app.menu.models import MenuItem


@admin.register(MenuItem)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'parent']
    search_fields = ['name']
