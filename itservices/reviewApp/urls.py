from . import views
from django.urls import path
from .views import PostListView, PostDetailView

urlpatterns =[
	path('', views.home, name='home'),
	path('about/', views.about, name='about'),
	path('contact/', views.contact, name='contact'),
	path('product/', views.product, name='product'),
	path('product/', PostListView.as_view(), name='product'),
	path('product/<int:pk>', PostDetailView.as_view(), name='product-detail'),
]