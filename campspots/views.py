from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.http import HttpResponseForbidden
from django.contrib import messages
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from .models import Campspot, Category
from django.db.models.functions import Lower

from .forms import CampspotForm


def all_campspots(request):
    """ A view to show all campspots, including sorting and search queries """

    campspots = Campspot.objects.filter(is_available=True)
    campspots_full = Campspot.objects.filter(is_available=False)
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

            if sortkey == 'category':
                sortkey = 'category__name'

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
                messages.error(request, "You didn't enter any search criteria!")
                return redirect(reverse('home'))

            queries = Q(county__icontains=query) | Q(description__icontains=query) | Q(name__icontains=query) | Q(postcode__icontains=query)
            campspots = campspots.filter(queries)

    current_sorting = f'{sort}_{direction}'

    context = {
        'campspots': campspots,
        'search_term': query,
        'current_categories': categories,
        'current_sorting': current_sorting,
        'campspots_full': campspots_full,

    }

    return render(request, 'campspots/campspots.html', context)


def campspot_detail(request, campspot_id):
    """ A view to show individual campspot details """

    campspot = get_object_or_404(Campspot, pk=campspot_id)

    context = {
        'campspot': campspot,
        'can_edit': request.user.is_superuser or (request.user == campspot.owner)
    }

    return render(request, 'campspots/campspot_detail.html', context)


@login_required
def add_campspot(request):
    """ Add a campspot or campspot template for business users to edit """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only campspot owners can do that.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = CampspotForm(request.POST, request.FILES)
        if form.is_valid():
            campspot = form.save()
            messages.success(request, 'Successfully added campspot!')
            return redirect(reverse('campspot_detail', args=[campspot.id]))
        else:
            messages.error(request, 'Failed to add campspot. Please ensure the form is valid.')
    else:
        form = CampspotForm()
        template = 'campspots/add_campspot.html'
    context = {
        'form': form,

    }

    return render(request, template, context)


@login_required
def edit_campspot(request, campspot_id):
    """ Edit a campspot authorised by superuser or campspot owner """

    campspot = get_object_or_404(Campspot, pk=campspot_id)
    if not (request.user.is_superuser or (request.user == campspot.owner)):
        # messages.error(request, 'Sorry, only hosts can do that.')
        # return redirect(reverse('home'))
        return HttpResponseForbidden()

    if request.method == 'POST':
        form = CampspotForm(request.POST, request.FILES, instance=campspot)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated campspot!')
            return redirect(reverse('campspot_detail', args=[campspot.id]))
        else:
            messages.error(request, 'Failed to update campspot. Please ensure the form is valid.')
    else:
        # messages.info(request, f'You are editing {campspot.name}')

        form = CampspotForm(instance=campspot)
    template = 'campspots/edit_campspot.html'
    context = {
        'form': form,
        'campspot': campspot,
    }

    return render(request, template, context)


@login_required
def delete_campspot(request, campspot_id):
    """ Delete a campspot, superuser only """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, extra authorisation is needed to do that.')
        return redirect(reverse('home'))
    campspot = get_object_or_404(Campspot, pk=campspot_id)
    campspot.delete()
    messages.success(request, 'Campspot deleted!')
    return redirect(reverse('campspots'))
