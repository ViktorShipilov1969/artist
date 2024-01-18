from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('users/', include('users.urls', namespace='users')),
    path('about/', include('about.urls', namespace='about')),
    path('artworks/', include('artworks.urls', namespace='artworks')),
    path('', include('blog.urls', namespace='blog')),
    path('admin/', admin.site.urls),
    path('auth/', include('django.contrib.auth.urls')),
]
urlpatterns += static(
    settings.MEDIA_URL,
    document_root=settings.MEDIA_ROOT
)
