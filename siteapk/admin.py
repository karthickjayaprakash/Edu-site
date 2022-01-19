from django.contrib import admin
from .models import Customer, book

# Register your models here.


admin.site.register(book)
admin.site.register(Customer)


