from django.shortcuts import render, redirect
from .models import Product


# Create your views here.

def home(request):
    products = Product.objects.all()
    return render(request, 'shop/home.html', {'products': products})

def category1(request):
    return render(request, 'shop/category1.html')

def category2(request):
    return render(request, 'shop/category2.html')

def category3(request):
    return render(request, 'shop/category3.html')

def category_products(request, category):
    products = Product.objects.filter(category=category)  # Filter products by category
    return render(request, 'shop/category.html', {'products': products, 'category': category})






