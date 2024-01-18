from django.urls import path

from . import views


app_name = 'artworks'

urlpatterns = [
    path('gallery/', views.gallery, name='gallery'),
    path('gallery/<int:artwork_id>', views.artwork_details, name='artwork_details'),
]
