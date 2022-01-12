from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from django.contrib.auth.models import Group

from .models import *
from .forms import CreateUserForm, CustomerForm, FarmerForm, WorkerForm, MarketForm, KitForm
# from .filters import PhoneFilter, HomePhoneFilter
from .decorators import unauthenticated_user, allowed_users, admin_only


# Create your views here.

def home(request):
	worker = Worker.objects.all()
	farmer = Farmer.objects.all()
	customer = Customer.objects.all()
	market = Farmermarket.objects.all()
	kit = Farmerkit.objects.all()


	tworker = worker.count()
	tcustomer = customer.count()
	tfarmer = farmer.count()
	tmarket = market.count()
	tkit = kit.count()
	tproduct = tmarket + tkit
	context = {'tworker': tworker, 'tfarmer': tfarmer, 'tcustomer': tcustomer, 'tproduct': tproduct}
	return render(request, 'home.html', context)

@unauthenticated_user
def signUp(request):
	form =  CreateUserForm()

	if request.method == 'POST':
		form = CreateUserForm(request.POST)
		if form.is_valid():
			user = form.save()

			username = form.cleaned_data.get('username')
			# group = Group.objects.get(name = 'customer')
			# user.groups.add(group)
			Person.objects.create(
				user=user,
				)

			# messages.success(request, 'Account was created for ' + username)
			return redirect('Category')

	context = {'form': form}
	return render(request, 'signup.html', context)



# @login_required(login_url = 'Login')
# @allowed_users(allowed_roles = ['owner'])
def category(request):
	context = {}
	return render(request, 'category.html', context)

@login_required(login_url = 'Login')
def signUpC(request):
	form =  CustomerForm()

	if request.method == 'POST':
		form = CustomerForm(request.POST)
		if form.is_valid():
			user = form.save()

			name = form.cleaned_data.get('name')
			group = Group.objects.get(name = 'customer')
			group.user_set.add(request.user)
			# Customer.objects.create(
			# 	usern=user,
			# 	)
			user.usern = Person.objects.get(user = request.user)
			form.save()

			# messages.success(request, 'Account was created for ' + username)
			return redirect('Signin')

	context = {'form': form}
	return render(request, 'customer_form.html', context)


@login_required(login_url = 'Login')
def signUpF(request):
	form =  FarmerForm()

	if request.method == 'POST':
		form = FarmerForm(request.POST)
		if form.is_valid():
			user = form.save()

			name = form.cleaned_data.get('name')
			group = Group.objects.get(name = 'farmer')
			group.user_set.add(request.user)
			# Customer.objects.create(
			# 	usern=user,
			# 	)
			user.usern = Person.objects.get(user = request.user)
			form.save()

			# messages.success(request, 'Account was created for ' + username)
			return redirect('Signin')

	context = {'form': form}
	return render(request, 'farmer_form.html', context)


@login_required(login_url = 'Login')
def signUpW(request):
	form =  WorkerForm()

	if request.method == 'POST':
		form = WorkerForm(request.POST)
		if form.is_valid():
			user = form.save()

			name = form.cleaned_data.get('name')
			group = Group.objects.get(name = 'worker')
			group.user_set.add(request.user)
			# Customer.objects.create(
			# 	usern=user,
			# 	)
			user.usern = Person.objects.get(user = request.user)
			form.save()

			# messages.success(request, 'Account was created for ' + username)
			return redirect('Signin')

	context = {'form': form}
	return render(request, 'worker_form.html', context)
	
@unauthenticated_user
def signIn(request):
    if request.method == 'POST':
    	username = request.POST.get('username')
    	password = request.POST.get('password')

    	user = authenticate(request, username = username, password = password)
    	if user is not None:
    		login(request, user) 
    		return redirect('Home')
    	else:
    		messages.info(request, 'Username or Password is incorrect ')
    context = {}
    return render(request, 'signin.html', context)
 
def logoutpage(request):
	logout(request)
	return redirect('Home')


@login_required(login_url = 'Login')
# @allowed_users(allowed_roles = ['owner'])
def farmerForm(request):

	context = {}
	return render(request, 'farmer_form.html', context)


@login_required(login_url = 'Login')
# @allowed_users(allowed_roles = ['owner'])
def customerForm(request):

	context = {}
	return render(request, 'customer_form.html', context)


@login_required(login_url = 'Login')
# @allowed_users(allowed_roles = ['owner'])
def workerForm(request):

	context = {}
	return render(request, 'worker_form.html', context)


def farmerKit(request):
	kit = Farmerkit.objects.all()

	context = {'kit': kit}
	return render(request, 'farmer_kit.html', context)


def farmerMarket(request):
	market = Farmermarket.objects.all()
	context = {'market': market}
	return render(request, 'farmer_market.html', context)


def hire(request):
	worker = Worker.objects.all()

	context = {'worker': worker}
	return render(request, 'hire.html', context)

def account(request):
	account = Worker.objects.all()

	context = {'account': account}
	return render(request, 'account.html', context)


@login_required(login_url = 'Login')
@allowed_users(allowed_roles = ['farmer'])
def kitForm(request):
	context = {}
	return render(request, 'farmer_kit.html', context)

@login_required(login_url = 'Login')
@allowed_users(allowed_roles = ['farmer', 'admin'])
def formMarket(request, pk):
	# person = Person.objects.get(user = pk)
	form = MarketForm()

	if request.method == 'POST':

		form = MarketForm(request.POST, request.FILES)
		# form.instance.owner = request.user
		if form.is_valid():
			print("add")
			form = form.save(commit = False)
			form.sname = Person.objects.get(user = request.user)
			form.save()
			return redirect('Farmermarket')

	context = {'form': form}
	return render(request, 'market_form.html', context)



@login_required(login_url = 'Login')
@allowed_users(allowed_roles = ['admin', 'farmer'])
# @admin_only
def formKit(request):
	# person = Person.objects.get(user = pk)
	form = KitForm()

	if request.method == 'POST':

		form = KitForm(request.POST, request.FILES)
		# form.instance.owner = request.user
		if form.is_valid():
			print("add")
			form = form.save(commit = False)
			# form.sname = Person.objects.get(user = request.user)
			form.save()
			return redirect('Farmerkit')

	context = {'form': form}
	return render(request, 'kit_form.html', context)

