from .models import Product, Review
from django.shortcuts import render, get_object_or_404
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

#def review(request):
#	review_item= {
#		'reviews': Review.objects.all()
#	}
#	return render(request, 'reviewApp/review.html', review_item)

class PostListView(ListView):
	model = Product
	template_name = 'reviewApp/product.html'
	context_object_name = 'products'
	ordering = ['-name']

class PostDetailView(DetailView):
	model = Product

class ProductReviewsListView(ListView):
	#model = Review
	context_object_name = 'object'
	template_name = 'reviewApp/reviews.html'
	queryset = Review.objects.all()

	def get_context_data(self, **kwargs):
		productName = self.kwargs['pk']
		context = super(ProductReviewsListView, self).get_context_data(**kwargs)
		context['reviews'] = Review.objects.filter(product=productName)
		context['products'] = Product.objects.filter(id=productName)
		return context

	#def get_context_data(self, **kwargs):
	#	context = super(ProductReviewsListView, self).get_context_data(**kwargs)
    #	some_data = Product.objects.all()
    #	context.update({'some_data': some_data})
    #	return context

	#def get_queryset(self): #Get a list of review for a specific product
	#	product=get_object_or_404(Product, name=self.kwargs.get('name'))
	#	#return Review.objects.filter(product=product).order_by('-rating')

	#def get_context_data(self, **kwargs):
	#	context = super(ProductReviewsListView, self).get_context_data(**kwargs)
	#	context['reviews'] = Review.objects.filter(product=product).order_by('-rating')