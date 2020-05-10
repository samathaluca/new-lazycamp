from django.shortcuts import render, redirect

# Create your views here.

def view_book(request):
    """ A view that renders the book contents page """

    return render(request, 'book/book.html')

def add_to_book(request, item_id):
    """ Add the camp spot selection to book """

    stuff = int(request.POST.get('stuff'))
    redirect_url = request.POST.get('redirect_url')
    book = request.session.get('book', {})

    if item_id in list(book.keys()):
        book[item_id] += stuff
    else:
        book[item_id] = stuff

    request.session['book'] = book
    return redirect(redirect_url)
