from django.conf import settings
from django.core.paginator import Paginator
from django.shortcuts import render

from .models import Artwork


def gallery(request):
    artworks_list = Artwork.objects.all()
    paginator = Paginator(artworks_list, settings.ARTWORKS_ON_PAGE)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'page_obj': page_obj,
    }
    return render(request, 'artworks/gallery.html', context)


def artwork_details(request, artwork_id):
    artwork = Artwork.objects.get(id=artwork_id)
    context = {
        'artwork': artwork,
    }
    return render(request, 'artworks/artwork_details.html', context)
