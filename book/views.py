  
from django.shortcuts import render, redirect, reverse, HttpResponse, get_object_or_404

from django.contrib import messages

from campspots.models import Campspot
# Create your views here and here.


def view_book(request):
    """ A view that renders the book contents page """

    return render(request, 'book/book.html')


def add_to_book(request, item_id):
    """ Add a booking """

    campspot = get_object_or_404(Campspot, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    booking_date = request.POST.get('booking_date')
    number_nights = int(request.POST.get('number_nights'))
    # print(booking_date)
    # print(number_nights)
    redirect_url = request.POST.get('redirect_url')
    size = None

    if 'booking_date' in request.POST:
        date = request.POST['booking_date']
    book = request.session.get('book', {})
    if date:
        if item_id in list(book.keys()):
            print(date)
            print(book)
            print(book[item_id]['items_by_date'].keys())
            if date in book[item_id]['items_by_date'].keys():
                book[item_id]['items_by_date'][date]['number_people'] += quantity
                book[item_id]['items_by_date'][date]['number_nights'] += number_nights
                messages.success(request, f'Updated date {date.upper()} {campspot.name} quantity to {book[item_id]["items_by_date"][date]}')
            else:
                book[item_id]['items_by_date'][date] = {}
                book[item_id]['items_by_date'][date]['number_people'] = quantity
                book[item_id]['items_by_date'][date]['number_nights'] = number_nights
                messages.success(request, f'Added date {date.upper()} {campspot.name} to book')
        else:
            book[item_id] = {'items_by_date': {date: {'number_people': quantity, 'number_nights': number_nights}}}
            messages.success(request, f'Added date {date.upper()} {campspot.name} to book')


    print(book)
    request.session['book'] = book
    return redirect(redirect_url)


def adjust_book(request, item_id):
    """Adjust the quantity of the specified campspot to the specified amount"""
    campspot = get_object_or_404(Campspot, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    size = None
    if 'pitch_sizes' in request.POST:
        size = request.POST['pitch_sizes']
    book = request.session.get('book', {})

    if size:
        if quantity > 0:
            book[item_id]['items_by_size'][size] = quantity
            messages.success(request, f'Updated size {size.upper()} {campspot.name} quantity to {book[item_id]["items_by_size"][size]}')
        else:
            del book[item_id]['items_by_size'][size]
            if not book[item_id]['items_by_size']:
                book.pop(item_id)
                messages.success(request, f'Removed size {size.upper()} {campspot.name} from your booking')
    else:
        if quantity > 0:
            book[item_id] = quantity
            messages.success(request, f'Updated {campspot.name} quantity to {book[item_id]}')
        else:
            book.pop(item_id)
            messages.success(request, f'Removed {campspot.name} from your booking')

    request.session['book'] = book
    return redirect(reverse('view_book'))


def remove_from_book(request, item_id):
    """Remove the item from booking"""

    try:
        campspot = get_object_or_404(Campspot, pk=item_id)
        size = None
        if 'pitch_sizes' in request.POST:
            size = request.POST['pitch_sizes']
        book = request.session.get('book', {})

        if size:
            del book[item_id]['items_by_size'][size]
            if not book[item_id]['items_by_size']:
                book.pop(item_id)
                messages.success(request, f'Removed size {size.upper()} {campspot.name} from your booking')
        else:
            book.pop(item_id)
            messages.success(request, f'Removed {campspot.name} from your booking')
        request.session['book'] = book
        return HttpResponse(status=200)

    except Exception as e:
        return HttpResponse(status=500)
        
