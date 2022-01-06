from django.shortcuts import render, redirect
from django.http import HttpResponse

# Create your views here.

def home(request):

	context = {}
	return render(request, 'home.html', context)

def signUp(request):

	context = {}
	return render(request, 'signup.html', context)



def signIn(request):

	context = {}
	return render(request, 'signin.html', context)


def farmerKit(request):

	context = {}
	return render(request, 'farmer_kit.html', context)


def farmerMarket(request):

	context = {}
	return render(request, 'farmer_market.html', context)