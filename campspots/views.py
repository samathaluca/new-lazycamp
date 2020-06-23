from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from .models import Campspot, Category

# Create your views here.


def all_campspots(request):
    """ A view to show all campspots, including sorting and search queries """

    campspots = Campspot.objects.all()
    query = None
    categories = None
    sort = None
    direction = None

    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                campspots = campspots.annotate(lower_name=Lower('name'))

            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            campspots = campspots.order_by(sortkey)

        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            campspots = campspots.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                # messages.error(request, "You didn't enter any search criteria!")
                return redirect(reverse('campspots'))

            queries = Q(county__icontains=query) | Q(description__icontains=query)
            campspots = campspots.filter(queries)

    current_sorting = f'{sort}_{direction}'

    context = {
        'campspots': campspots,
        'search_term': query,
        'current_categories': categories,
        'current_sorting': current_sorting,
    }

    return render(request, 'campspots/campspots.html', context)


def campspot_detail(request, campspot_id):
    """ A view to show individual product details """

    campspot = get_object_or_404(Campspot, pk=campspot_id)

    context = {
        'campspot': campspot,
    }

    return render(request, 'campspots/campspot_detail.html', context)
