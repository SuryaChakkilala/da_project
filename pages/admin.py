from django.contrib import admin
from .models import Facility, Vehicle, Cargo, Goods

# Register your models here.
admin.site.register(Facility)
admin.site.register(Vehicle)
admin.site.register(Cargo)
admin.site.register(Goods)