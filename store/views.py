from django.shortcuts import render, get_object_or_404
from .models import Product, Category
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.core.files.storage import FileSystemStorage
from django.contrib.auth.decorators import user_passes_test

def home(request):
    categories = Category.objects.all()
    products = Product.objects.all()
    return render(request, 'store/home.html', {'categories': categories, 'products': products})

def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'store/product_detail.html', {'product': product})

def is_staff(user):
    return user.is_staff

# Removed add_product view for buyer-only site
