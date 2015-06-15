# -*- coding: utf-8 -*-
from django.contrib import admin
from models import Post, Subscribe


class PostAdmin(admin.ModelAdmin):
    list_display = ('author', 'created', 'title',)
    search_fields = ('title', 'body', )


class SubscribeAdmin(admin.ModelAdmin):
    list_display = ('author', 'reader', 'date_joined',)


admin.site.register(Post, PostAdmin)
admin.site.register(Subscribe, SubscribeAdmin)
