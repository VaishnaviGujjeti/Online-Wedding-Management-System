from django.contrib import admin
from .models import City, Category, Service, Booking, Contact

admin.site.register(City)
admin.site.register(Category)
admin.site.register(Service)
admin.site.register(Booking)
admin.site.register(Contact)

