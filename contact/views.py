from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.

from .forms import ContactForm

def contact(request):
    templete = 'contact.html'

    if request.method == "POST":
        form = ContactForm(request.POST)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')

    else:
        form = ContactForm()

    context = {
        'form': form,
    }
    return render(request, templete, context)
