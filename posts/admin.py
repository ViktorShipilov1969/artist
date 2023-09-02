from django.contrib import admin
from .models import Post

class PostAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title', 'text', 'pub_date',)
    list_editable = ('title',)
    search_fields = ('text', 'title')
    list_filter = ('pub_date',)


admin.site.register(Post, PostAdmin)
