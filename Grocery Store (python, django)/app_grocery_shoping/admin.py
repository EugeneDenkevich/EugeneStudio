from django.contrib import admin

from .models import User, Delivery, Cart, Product

admin.site.register(User)
admin.site.register(Delivery)
admin.site.register(Cart)
admin.site.register(Product)