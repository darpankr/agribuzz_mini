from django.contrib import admin

from .models import *

# Register your models here.

# admin.site.register(People)
admin.site.register(Person)
admin.site.register(Customer)
admin.site.register(Farmer)
admin.site.register(Worker)
admin.site.register(Farmerkit)
admin.site.register(Farmermarket)