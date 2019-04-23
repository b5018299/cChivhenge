from django.urls import reverse
from .models import Product, Review
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

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
		productId = self.kwargs['pk']
		product=get_object_or_404(Product, id=productId) #Shows the user a 404 if the product doesnt exist
		context = super(ProductReviewsListView, self).get_context_data(**kwargs)
		context['reviews'] = Review.objects.filter(product=productId) #do an order by?
		context['products'] = Product.objects.filter(id=productId)
		return context

class CreateReview(LoginRequiredMixin, CreateView):
	model = Review
	fields = ['rating', 'review_text']

	def form_valid(self, form, **kwargs):
		productId = self.kwargs['pk']
		form.instance.author = self.request.user
		form.instance.product = Product.objects.get(id=productId)
		return super().form_valid(form)

class UpdateReview(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
	model = Review
	fields = ['rating', 'review_text']

	def test_func(self):
		review = self.get_object()
		if self.request.user == review.author:
			return True
		return False

class DeleteReview(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
	model = Review

	# def redirect(self, **kwargs):
	# 	success_url = '/product', kwargs={'pk': self.product.id}

	# def get_absolute_url(self):
	# 	#success_url = '/review', kwargs={'pk': self.product.id}
	# 	return reverse('reviews', kwargs={'pk': self.product.id}) #after creating review, redirect to product page

	def get_success_url(self):
		#slug = self.kwargs['slug']
		review = self.get_object()
		return reverse('reviews', kwargs={'pk': review.product.id})

	def test_func(self):
		review = self.get_object()
		if self.request.user == review.author:
			return True
		return False