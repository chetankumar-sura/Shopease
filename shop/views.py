from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ContactForm
# Create your views here.

def home(request):
    return render(request, 'shop/home.html')

def category1(request):
    return render(request, 'shop/category1.html')

def category2(request):
    return render(request, 'shop/category2.html')

def category3(request):
    return render(request, 'shop/category3.html')



def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Your message has been sent successfully!")
            return redirect('home')  # Redirect to home after submission
    else:
        form = ContactForm()

    return render(request, "shop/contact.html", {"form": form})

