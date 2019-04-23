from . import views
from django.urls import path
from .views import PostListView, PostDetailView, ProductReviewsListView, CreateReview, UpdateReview, DeleteReview

urlpatterns =[
	path('', views.home, name='home'),
	path('about/', views.about, name='about'),
	path('contact/', views.contact, name='contact'),
	path('product/', views.product, name='product'),
	path('product/', PostListView.as_view(), name='product'),
	#path('product/<int:pk>', PostDetailView.as_view(), name='product-detail'),
	path('product/<int:pk>', ProductReviewsListView.as_view(), name='reviews'),
	path('review/new/<int:pk>', CreateReview.as_view(), name='review-create'), #passes product id
	path('review/<int:pk>/update/', UpdateReview.as_view(), name='review-update'),
	path('review/<int:pk>/delete/', DeleteReview.as_view(), name='review-delete'),
	
]