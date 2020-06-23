from django.shortcuts import render
from .models import Campspot

# Create your views here.


def all_campspots(request):
    """ A view to show all campspotss, including sorting and search queries """

    campspots = Campspot.objects.all()

    context = {
        'campspots': campspots,
    }

    return render(request, 'campspots/campspots.html', context)
