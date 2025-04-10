from django.contrib import admin

from main_app.models import Product
#admin.site.register(Product)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price']
    list_filter = ['name', 'price']
    search_fields = ['category', 'name']
    fields = [
        ('name', 'price'),
        ('category', 'supplier')
    ]