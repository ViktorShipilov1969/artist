from django.urls import path

from . import views


app_name = 'blog'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('posts/', views.blog, name='posts'),
    path('posts/<int:post_id>', views.post_details, name='post_detail'),
    path('videos/', views.videos, name='videos'),
    path('video/<int:video_id>', views.video_details, name='video_details')
]
