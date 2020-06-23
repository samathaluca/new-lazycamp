from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from .models import Campspot

# Create your views here.


def all_campspots(request):
    """ A view to show all campspots, including sorting and search queries """

    campspots = Campspot.objects.all()
    query = None

    if request.GET:
        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                # messages.error(request, "You didn't enter any search criteria!")
                return redirect(reverse('campspots'))
            
            queries = Q(county__icontains=query) | Q(description__icontains=query )
            campspots = campspots.filter(queries)

    context = {
        'campspots': campspots,
        'search_term': query,
    }

    return render(request, 'campspots/campspots.html', context)


def campspot_detail(request, campspot_id):
    """ A view to show individual product details """

    campspot = get_object_or_404(Campspot, pk=campspot_id)

    context = {
        'campspot': campspot,
    }

    return render(request, 'campspots/campspot_detail.html', context)
