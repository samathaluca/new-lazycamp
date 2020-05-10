from decimal import Decimal
from django.conf import settings

def book_contents(request):

    book_items = []
    total = 0
    product_count = 0

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