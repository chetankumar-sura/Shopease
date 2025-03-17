from django.shortcuts import render, redirect
from .models import Product
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import SignupForm

# Create your views here.

def home(request):
    # products = Product.objects.all()
    # return render(request, 'shop/home.html', {'products': products})
    return render(request, 'shop/home.html')

def category_products(request, category):
    products = Product.objects.filter(category=category)  # Filter products by category
    return render(request, 'shop/category.html', {'products': products, 'category': category})

def signup_view(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = SignupForm()
    return render(request, 'shop/signup.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'shop/login.html', {'error': 'Invalid Credentials'})
        
    return render(request, 'shop/login.html')

@login_required
def profile_view(request):
    return render(request, 'shop/profile.html')


def logout_view(request):
    logout(request)
    return redirect('home')
 




