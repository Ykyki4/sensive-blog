from django.contrib import admin
from blog.models import Post, Tag, Comment


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    raw_id_fields = ['likes', 'author', 'tags']


@admin.register(Comment)
class Comment(admin.ModelAdmin):
    raw_id_fields = ['post', 'author']
    list_display = ['post', 'author']
admin.site.register(Tag)

