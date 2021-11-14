from django.contrib import admin
from blog.models import Blog, Category

class BlogAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'body',
        'posted',
        'category',
        'image',
    )

    ordering = ('title',)

class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )

admin.site.register(Blog, BlogAdmin)
admin.site.register(Category, CategoryAdmin)
