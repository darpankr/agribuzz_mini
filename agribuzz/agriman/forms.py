
from django.forms import ModelForm

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

from .models import *

class CreateUserForm(UserCreationForm):
	class Meta:
		model = User
		fields = ['username', 'email', 'password1', 'password2']


class CustomerForm(ModelForm):
	class Meta:
		model = Customer
		fields = '__all__'
		exclude = ['usern']

class FarmerForm(ModelForm):
	class Meta:
		model = Farmer
		fields = '__all__'
		exclude = ['usern']

class WorkerForm(ModelForm):
	class Meta:
		model = Worker
		fields = '__all__'
		exclude = ['usern']


class KitForm(ModelForm):
	class Meta:
		model = Farmerkit
		fields = '__all__'
		# exclude = ['owner']

class MarketForm(ModelForm):
	class Meta:
		model = Farmermarket
		fields = '__all__'
		exclude = ['sname']