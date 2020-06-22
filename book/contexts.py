from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from products.models import Product
import datetime


def book_contents(request):

    book_items = []
    total = 0
    product_count = 0
    book = request.session.get('book', {})

    for item_id, item_data in book.items():
        if isinstance(item_data, int):
            product = get_object_or_404(Product, pk=item_id)
            total += item_data * product.price
            product_count += item_data
            book_items.append({
                'item_id': item_id,
                'quantity': item_data,
                'product': product,
                # 'number_nights': number_nights,
                })

            #     elseif:
            # product = get_object_or_404(Product, pk=item_id)
            # for date, quantity in item_data['items_by_date'].items():
            #     total += quantity * product.price
            #     product_count += quantity
            #     book_items.append({
            #         'item_id': item_id,
            #         'quantity': quantity,
            #         'product': product,
            #         'date': date,
            #   #     })
        else:
            product = get_object_or_404(Product, pk=item_id)
            # for size, quantity in item_data['items_by_size'].items():
            for date, booking_info in item_data['items_by_date'].items():
                # total += booking_info['number_people'] * product.price
                total += booking_info["number_people"] * product.price * booking_info["number_nights"]
                product_count += booking_info['number_people']
                book_items.append({
                    'item_id': item_id,
                    'quantity': booking_info['number_people'],
                    'product': product,
                    'date': datetime.datetime.strptime(date, '%Y-%m-%d').date,
                    'number_nights': booking_info['number_nights'],
                })

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
        'product_count': product_count,
        'night': night,
        'free_night_delta': free_night_delta,
        'free_night_threshold': settings.FREE_NIGHT_THRESHOLD,
        'grand_total': grand_total,
    }

    return context
