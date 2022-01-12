from django.urls import path
from .import views


urlpatterns = [
	
	path('', views.home, name = 'Home'),
	path('signin/', views.signIn, name = 'Signin'),
	path('signup/', views.signUp, name = 'Signup'),
	path('category/', views.category, name = 'Category'),
	path('signupc/', views.signUpC, name = 'Signupc'),
	path('signupf/', views.signUpF, name = 'Signupf'),
	path('signupw/', views.signUpW, name = 'Signupw'),
	path('logout/', views.logoutpage, name = 'Logout'),
	path('customerf/', views.customerForm, name = 'Customerform'),
	path('farmerf/', views.farmerForm, name = 'Farmerform'),
	path('workerf/', views.workerForm, name = 'Workerform'),
	path('farmermarket/', views.farmerMarket, name = 'Farmermarket'),
	path('formmarket/<int:pk>/', views.formMarket, name = 'Formmarket'),
	path('farmerkit/', views.farmerKit, name = 'Farmerkit'),
	path('formkit/', views.formKit, name = 'Formkit'),
	path('hire/', views.hire, name = 'Hire'),
	path('account/', views.account, name = 'Account'),
]