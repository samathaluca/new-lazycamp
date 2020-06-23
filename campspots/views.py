from django.shortcuts import render, get_object_or_404
from .models import Campspot

# Create your views here.


def all_campspots(request):
    """ A view to show all campspots, including sorting and search queries """

    campspots = Campspot.objects.all()

    context = {
        'campspots': campspots,
    }

    return render(request, 'campspots/campspots.html', context)


def campspot_detail(request, campspot_id):
    """ A view to show campspot details """

    campspot = get_object_or_404(Campspot, pk=campspot_id)

    context = {
        'campspot': campspot,
    }

    return render(request, 'campspots/campspot_detail.html', context)



# def campspots(request):
#     """ A view to show individual product dates """

#     # product = get_object_or_404(Product, pk=product_id)
#     campspots_available = Campspot.objects.filter(is_available=True)
#     context = {
#         'campspots_available': campspots_available,
#     }

#     return render(request, 'campspots/campspots_available.html', context)
