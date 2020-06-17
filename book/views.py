from django.shortcuts import render, redirect, reverse, HttpResponse, get_object_or_404

from django.contrib import messages

from products.models import Product
# Create your views here.


def view_book(request):
    """ A view that renders the book contents page """

    return render(request, 'book/book.html')


def add_to_book(request, item_id):
    """ Add a booking """

    product = get_object_or_404(Product, pk=item_id)
    # product = Product.objects.get(pk=item_id)
    quantity = int(request.POST.get('quantity'))
    booking_date = request.POST.get('booking_date')
    print(booking_date)
    redirect_url = request.POST.get('redirect_url')
    size = None


    if 'booking_date' in request.POST:
        date = request.POST['booking_date']
    book = request.session.get('book', {})
    if date:
        if item_id in list(book.keys()):
            if date in book[item_id]['items_by_date'].keys():
                book[item_id]['items_by_date'][date] += quantity
                messages.success(request, f'Updated date {date.upper()} {product.name} quantity to {book[item_id]["items_by_date"][date]}')
            else:
                book[item_id]['items_by_date'][date] = quantity
                messages.success(request, f'Added date {date.upper()} {product.name} to book')
        else:
            book[item_id] = {'items_by_date': {date: quantity}}
            messages.success(request, f'Added date {date.upper()} {product.name} to book')

    if 'pitch_sizes' in request.POST:
        size = request.POST['pitch_sizes']
    book = request.session.get('book', {})
    if size:
        if item_id in list(book.keys()):
            if size in book[item_id]['items_by_size'].keys():
                book[item_id]['items_by_size'][size] += quantity
                messages.success(request, f'Updated size {size.upper()} {product.name} quantity to {book[item_id]["items_by_size"][size]}')
            else:
                book[item_id]['items_by_size'][size] = quantity
                messages.success(request, f'Added size {size.upper()} {product.name} to book')
        else:
            book[item_id] = {'items_by_size': {size: quantity}}
            messages.success(request, f'Added size {size.upper()} {product.name} to book')
    else:
        if item_id in list(book.keys()):
            book[item_id] += quantity
            messages.success(request, f'Updated {product.name} quantity to {book[item_id]}')
        else:
            book[item_id] = quantity
            messages.success(request, f'Added {product.name} to book')

    request.session['book'] = book
    return redirect(redirect_url)


def adjust_book(request, item_id):
    """Adjust the quantity of the specified product to the specified amount"""
    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    size = None
    if 'pitch_sizes' in request.POST:
        size = request.POST['pitch_sizes']
    book = request.session.get('book', {})

    if size:
        if quantity > 0:
            book[item_id]['items_by_size'][size] = quantity
            messages.success(request, f'Updated size {size.upper()} {product.name} quantity to {book[item_id]["items_by_size"][size]}')
        else:
            del book[item_id]['items_by_size'][size]
            if not book[item_id]['items_by_size']:
                book.pop(item_id)
                messages.success(request, f'Removed size {size.upper()} {product.name} from your booking')
    else:
        if quantity > 0:
            book[item_id] = quantity
            messages.success(request, f'Updated {product.name} quantity to {book[item_id]}')
        else:
            book.pop(item_id)
            messages.success(request, f'Removed {product.name} from your booking')

    request.session['book'] = book
    return redirect(reverse('view_book'))


def remove_from_book(request, item_id):
    """Remove the item from booking"""

    try:
        product = get_object_or_404(Product, pk=item_id)
        size = None
        if 'pitch_sizes' in request.POST:
            size = request.POST['pitch_sizes']
        book = request.session.get('book', {})

        if size:
            del book[item_id]['items_by_size'][size]
            if not book[item_id]['items_by_size']:
                book.pop(item_id)
                messages.success(request, f'Removed size {size.upper()} {product.name} from your booking')
        else:
            book.pop(item_id)
            messages.success(request, f'Removed {product.name} from your booking')
        request.session['book'] = book
        return HttpResponse(status=200)

    except Exception as e:
        return HttpResponse(status=500)
