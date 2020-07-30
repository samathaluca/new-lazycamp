from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from campspots.models import Campspot
import datetime


def book_contents(request):
    '''add bookings to session'''

    book_items = []
    total = 0
    campspot_count = 0
    book = request.session.get('book', {})

    for item_id, item_data in book.items():
        if isinstance(item_data, int):
            campspot = get_object_or_404(Campspot, pk=item_id)
            total += item_data * campspot.price
            campspot_count += item_data
            book_items.append({
                'item_id': item_id,
                'quantity': item_data,
                'campspot': campspot,
                })


        else:
            campspot = get_object_or_404(Campspot, pk=item_id)
            for date, booking_info in item_data['items_by_date'].items():
                total += booking_info["number_people"] * campspot.price * booking_info["number_nights"]
                campspot_count += booking_info['number_people']
                book_items.append({
                    'item_id': item_id,
                    'quantity': booking_info['number_people'],
                    'campspot': campspot,
                    'date': datetime.datetime.strptime(date, '%Y-%m-%d').date,
                    'number_nights': booking_info['number_nights'],
                })
    # Calculate and adds special offers from settings
    if total < settings.FREE_NIGHT_THRESHOLD:
        night = total * Decimal(settings.STANDARD_NIGHT_PERCENTAGE / 100)
        free_night_delta = settings.FREE_NIGHT_THRESHOLD - total
    else:
        night = 0
        free_night_delta = 0

    grand_total = night + total

    context = {
        'book_items': book_items,
        'total': total,
        'campspot_count': campspot_count,
        'night': night,
        'free_night_delta': free_night_delta,
        'free_night_threshold': settings.FREE_NIGHT_THRESHOLD,
        'grand_total': grand_total,
    }

    return context
