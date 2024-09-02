from django.shortcuts import render

def view_bag(request):
    """ A view that renders the bag page. """

    return render(request, 'bag/bag.html')

