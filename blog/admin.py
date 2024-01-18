from django.contrib import admin
from .models import Post, Video, Comment


class PostAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title', 'pub_date',)
    list_editable = ('title',)
    search_fields = ('text', 'title',)
    list_filter = ('pub_date',)


class VideoAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title',)
    list_editable = ('title',)
    search_fields = ('title', 'description',)


class CommentAdmin(admin.ModelAdmin):
    list_display = ('post', 'author', 'text', 'pub_date',)
    search_fields = ('post', 'author', 'text',)


admin.site.register(Post, PostAdmin)
admin.site.register(Video, VideoAdmin)
admin.site.register(Comment, CommentAdmin)
