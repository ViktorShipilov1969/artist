from django.contrib import admin
from .models import Artwork


class ArtworkAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title', 'completion_date', 'status', 'price',)
    list_editable = ('status',)
    search_fields = ('title',)
    list_filter = ('completion_date',)


admin.site.register(Artwork, ArtworkAdmin)
