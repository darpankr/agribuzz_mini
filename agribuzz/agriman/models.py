from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Person(models.Model):
	user = models.OneToOneField(User, null = True, blank = True, on_delete = models.CASCADE)
	# name = models.CharField(max_length = 100, null = True)
	# phone = models.CharField(max_length = 100, null = True)
	# email = models.CharField(max_length = 100, null = True)
	# profile_pic = models.ImageField(default = "aloki1.PNG", null = True, blank = True)
	date_created = models.DateTimeField(auto_now_add = True, null = True)

	def __str__(self):
		return str(self.user)


class Customer(models.Model):
	usern = models.OneToOneField(Person, null = True, blank = True, on_delete = models.CASCADE)
	name = models.CharField(max_length = 100, null = True)
	phone = models.CharField(max_length = 100, null = True)
	email = models.CharField(max_length = 100, null = True)
	state = models.CharField(max_length = 100, null = True)
	district = models.CharField(max_length = 100, null = True)
	pin = models.CharField(max_length = 100, null = True)
	bname = models.CharField(max_length = 100, null = True)
	accno = models.CharField(max_length = 100, null = True)
	ifsc = models.CharField(max_length = 100, null = True)
	profile_pic = models.ImageField(default = "aloki1.PNG", null = True, blank = True)
	date_created = models.DateTimeField(auto_now_add = True, null = True)

	def __str__(self):
		return str(self.name)

class Farmer(models.Model):
	usern = models.OneToOneField(Person, null = True, blank = True, on_delete = models.CASCADE)
	name = models.CharField(max_length = 100, null = True)
	phone = models.CharField(max_length = 100, null = True)
	email = models.CharField(max_length = 100, null = True)
	state = models.CharField(max_length = 100, null = True)
	district = models.CharField(max_length = 100, null = True)
	pin = models.CharField(max_length = 100, null = True)
	bname = models.CharField(max_length = 100, null = True)
	accno = models.CharField(max_length = 100, null = True)
	ifsc = models.CharField(max_length = 100, null = True)
	profile_pic = models.ImageField(default = "aloki1.PNG", null = True, blank = True)
	date_created = models.DateTimeField(auto_now_add = True, null = True)

	def __str__(self):
		return self.name

class Worker(models.Model):

	STATUS = (
		('active', 'active'),
		('inactive', 'inactive'),
		('hired', 'hired')
		)
	usern = models.OneToOneField(Person, null = True, blank = True, on_delete = models.CASCADE)
	name = models.CharField(max_length = 100, null = True)
	phone = models.CharField(max_length = 100, null = True)
	email = models.CharField(max_length = 100, null = True)
	state = models.CharField(max_length = 100, null = True)
	district = models.CharField(max_length = 100, null = True)
	pin = models.CharField(max_length = 100, null = True)
	bname = models.CharField(max_length = 100, null = True)
	accno = models.CharField(max_length = 100, null = True)
	ifsc = models.CharField(max_length = 100, null = True)
	dob = models.DateField(null = True)
	status = models.CharField(max_length = 20, null = True, choices = STATUS)
	exsalary = models.CharField(max_length = 10, null = True)
	profile_pic = models.ImageField(default = "aloki1.PNG", null = True, blank = True)
	date_created = models.DateTimeField(auto_now_add = True, null = True)

	def __str__(self):
		return self.name

class Farmerkit(models.Model):
	STATUS = (
		('in stock', 'In Stock'),
		('out of stock', 'Out Of Stock')
		)
	# s_name = models.OneToOneField(, null = True, blank = True, on_delete = models.CASCADE)
	# sname = models.ForeignKey(User, null = True, on_delete = models.SET_NULL)
	name = models.CharField(max_length = 100, null = True)
	price = models.FloatField(max_length = 100, null = True)
	desc = models.CharField(max_length = 100, null = True)
	status = models.CharField(max_length = 20, null = True, choices = STATUS)
	image = models.ImageField(default = "aloki1.PNG", null = True, blank = True)
	date_created = models.DateTimeField(auto_now_add = True, null = True)

	def __str__(self):
		return self.name


class Farmermarket(models.Model):

	STATUS = (
		('in stock', 'In Stock'),
		('out of stock', 'Out Of Stock')
		)
	CAT = (
		('vegetable', 'vegetable'),
		('fruits', 'fruits'),
		('crops', 'crops'),
		)
	# fn = models.ForeignKey(Farmer, null = True, on_delete = models.SET_NULL)
	sname = models.ForeignKey(Person, null = True, on_delete = models.SET_NULL)
	name = models.CharField(max_length = 100, null = True)
	price = models.FloatField(max_length = 100, null = True)
	desc = models.CharField(max_length = 100, null = True)
	quantity = models.CharField(max_length = 100, null = True)
	status = models.CharField(max_length = 20, null = True, choices = STATUS)
	cat = models.CharField(max_length = 20, null = True, choices = CAT)
	image = models.ImageField(default = "aloki1.PNG", null = True, blank = True)
	date_created = models.DateTimeField(auto_now_add = True, null = True)

	def __str__(self):
		return self.name


