from django.shortcuts import render, redirect

# Create your views here.

def view_book(request):
    """ A view that renders the book contents page """

    return render(request, 'book/book.html')

def add_to_book(request, item_id):
    """ Add the camp spot selection to book """

    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    size = None
    if 'product_size' in request.POST:
        size = request.POST['product_size']
    book = request.session.get('book', {})

    if size:
        if item_id in list(book.keys()):
            if size in book[item_id]['items_by_size'].keys():
                book[item_id]['items_by_size'][size] += quantity
            else:
                book[item_id]['items_by_size'][size] = quantity
        else:
            book[item_id] = {'items_by_size': {size: quantity}}
    else:
        if item_id in list(book.keys()):
            book[item_id] += quantity
        else:
            book[item_id] = quantity

    request.session['book'] = book
    return redirect(redirect_url)
