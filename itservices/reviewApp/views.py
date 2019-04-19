from .models import Product
from django.shortcuts import render
from django.views.generic import ListView, DetailView

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

class PostListView(ListView):
	model = Product
	template_name = 'reviewApp/product.html'
	context_object_name = 'products'
	ordering = ['-name']

class PostDetailView(DetailView):
	model = Product