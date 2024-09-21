from django.shortcuts import render
from .forms import ContactQueryForm

def contact(request):
    """ A view to return the contact page with a form """
    form = ContactQueryForm()

    if request.method == 'POST':
        form = ContactQueryForm(request.POST)
        if form.is_valid():
            form.save()

    return render(request, 'contact/contact.html', {'contact_query_form': form})
