from django.views.generic.base import TemplateView


class AboutView(TemplateView):
    template_name = 'about/about.html'


class ContactsView(TemplateView):
    template_name = 'about/contacts.html'
