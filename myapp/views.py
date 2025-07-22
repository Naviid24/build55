from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import ContactForm


def my_app_view(request):
    return HttpResponse("Hello, this is my app view!")


def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contact_thank_you')  # or show a success message
    else:
        form = ContactForm()
    return render(request, 'myapp/contact.html', {'form': form})