from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from products.models import Product

def book_contents(request):

    book_items = []
    total = 0
    product_count = 0
    book = request.session.get('book', {})

    for item_id, stuff in book.items():
        product = get_object_or_404(Product, pk=item_id)
        total += stuff * product.price
        product_count += stuff
        book_items.append({
            'item_id': item_id,
            'stuff': stuff,
            'product': product,
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