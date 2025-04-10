from django.contrib import admin
from .models import Profile, Product, Order


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    """Custom admin settings for Profile"""
    list_display = ('full_name', 'email', 'phone_number', 'is_active')
    search_fields = ('full_name', 'email')
    search_help_text = "Search by full name or email."


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    """Custom admin settings for Product"""
    list_display = ('name', 'price', 'in_stock', 'is_available')
    list_filter = ('is_available',)
    search_fields = ('name',)
    search_help_text = "Search by product name."


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    """Custom admin settings for Order"""
    list_display = ('profile', 'total_price', 'creation_date', 'is_completed')
    list_filter = ('is_completed',)
    search_fields = ('profile__full_name',)
    search_help_text = "Search by profile's full name."
