from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from .models import Product, Category

# Create your views here.

def all_products(request):
    """ A view to show all products, including sorting and search queries """

    products = Product.objects.all()
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
                products = products.annotate(lower_name=Lower('name'))

            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            products = products.order_by(sortkey)
            
        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            products = products.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You didn't enter any search criteria!")
                return redirect(reverse('products'))
            
            queries = Q(name__icontains=query) | Q(description__icontains=query)
            products = products.filter(queries)

    current_sorting = f'{sort}_{direction}'

    context = {
        'products': products,
        'search_term': query,
        'current_categories': categories,
        'current_sorting': current_sorting,
    }

    return render(request, 'products/products.html', context)


def product_detail(request, product_id):
    """ A view to show individual product details """

    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,
    }

    return render(request, 'products/product_detail.html', context)
    
# https://docs.djangoproject.com/en/3.0/topics/db/queries/

# By reading through the queries portion of the Django documentation.
# Getting back to the code using Q is actually quite simple.
# I'll set a variable equal to a Q object. Where the name contains the query.
# Or the description contains the query.
# The pipe here is what generates the or statement.
# And the i in front of contains makes the queries case insensitive.
# With those queries constructed.
# Now I can pass them to the filter method in order to actually filter the products.
# Now I'll add the query to the context. And in the template call it search term.
# And we'll start with it as none at the top of this view to ensure we don't get an error
# when loading the products page without a search term.
# Let's save that and test whether it works.
# I'll run a search for jeans, which as you can see returns all the jeans in our store.
# Now let's run a search for soft. To verify that we're also searching in descriptions.
# Looking at these items none of these first four contain the term soft in the product name.