from django.contrib import admin
from .models import Client, Book, BookCategory, Order
# Register your models here.

admin.site.register(Client)
admin.site.register(Book)
admin.site.register(BookCategory)
admin.site.register(Order)