from django.shortcuts import render
from .models import Product

def home(request):
	return render(request, 'reviewApp/home.html', {'title': 'Home'})
def about(request):
	return render(request, 'reviewApp/about.html', {'title': 'About'})
def contact(request):
	return render(request, 'reviewApp/contact.html', {'title': 'Contact'})
def product(request):
	return render(request, 'reviewApp/product.html', {'title': 'Product'})

def product(request):
	product_item= {
		'products': Product.objects.all() #defining what 'products' is
	}
	return render(request, 'reviewApp/product.html', product_item)