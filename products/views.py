from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.db.models.functions import Lower

from .models import Product, Category
from .forms import ProductForm

# Create your views here.


def all_products(request):
    """ A view to show all products, including sorting and search queries """

    products = Product.objects.all()
    # stops errors when loading page as input fields will be empty
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
            if sortkey == 'category':
                sortkey = 'category__name'
            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            products = products.order_by(sortkey)
# splits in to only products that contain searched for category(GET catergory)
# may be useful to get pnly products that have is available ticked
# for business users to control
        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            products = products.filter(category__name__in=categories)
# convert list of strings of category names passed through the URL in to loist of actual
# cat obj to access all their fields in template
# see contect to find list of category objects called current categories
            categories = Category.objects.filter(name__in=categories)
# search request, no input gives error message
        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request,
                               "You didn't enter any search criteria!")
                return redirect(reverse('products'))
# pending search term is present in name or description it will be returned
# maybe add category or postal district too
# i makes it non specific for example silv will still return silver
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


@login_required
def add_product(request):
    """ Add a product to the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save()
            messages.success(request, 'Successfully added product!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request, 'Failed to add product. Please ensure the form is valid.')
    else:
        form = ProductForm()
        template = 'products/add_product.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def edit_product(request, product_id):
    """ Edit a product in the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only hosts can do that.')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated product!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request, 'Failed to update product. Please ensure the form is valid.')
    else:
        # messages.info(request, f'You are editing {product.name}')

        form = ProductForm(instance=product)
        

        template = 'products/edit_product.html'
        context = {
            'form': form,
            'product': product,
    }

    return render(request, template, context)


@login_required
def delete_product(request, product_id):
    """ Delete a product from the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))
    # messages.info(request, f'You are editing {product.name}')
    product = get_object_or_404(Product, pk=product_id)
    product.delete()
    messages.success(request, 'Product deleted!')
    return redirect(reverse('products'))
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