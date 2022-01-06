from django.urls import path
from .import views


urlpatterns = [
	
	path('', views.home, name = 'Home'),
	path('signin/', views.signIn, name = 'Signin'),
	path('signup/', views.signUp, name = 'Signup'),
	path('farmermarket/', views.farmerMarket, name = 'Farmermarket'),
	path('farmerkit/', views.farmerKit, name = 'Farmerkit'),
]