from django.urls import path

from . import views


app_name = 'about'

urlpatterns = [
    path('about', views.AboutView.as_view(), name='about'),
    path('contacts', views.ContactsView.as_view(), name='contacts'),
]
