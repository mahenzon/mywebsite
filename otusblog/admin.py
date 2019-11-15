from django.contrib import admin

from .models import Publisher, Article


@admin.register(Publisher)
class PublisherAdmin(admin.ModelAdmin):
    list_display = 'id', 'first_name', 'last_name'


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = 'id', 'name', 'body_short'