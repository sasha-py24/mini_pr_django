from django.contrib import admin

# Register your models here.


from .models import Product, Categories


admin.site.register(Product)
admin.site.register(Categories)
