from django.shortcuts import render, redirect
from .forms import ContactForm


def home_view(request):
    return render(request, 'myapp/home.html')


def about_view(request):
    return render(request, 'myapp/about.html')


def kitchens_view(request):
    return render(request, 'myapp/kitchens.html')


def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contact_thank_you')  # or show a success message
    else:
        form = ContactForm()
    return render(request, 'myapp/contact.html', {'form': form})