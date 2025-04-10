from django.contrib import admin
from .models import Astronaut, Spacecraft, Mission


@admin.register(Astronaut)
class AstronautAdmin(admin.ModelAdmin):
    """Admin configuration for the Astronaut model."""
    list_display = ('name', 'spacewalks', 'is_active')  # Fields displayed in list view
    list_filter = ('is_active',)  # Filter by is_active status
    search_fields = ('name', 'phone_number')  # Enable search by name & phone number
    ordering = ('name',)  # Default ordering by name


@admin.register(Spacecraft)
class SpacecraftAdmin(admin.ModelAdmin):
    """Admin configuration for the Spacecraft model."""
    list_display = ('name', 'manufacturer', 'launch_date')  # Fields displayed in list view
    list_filter = ('capacity',)  # Filter by capacity
    search_fields = ('name',)  # Enable search by name
    readonly_fields = ('updated_at',)  # Make updated_at field read-only


@admin.register(Mission)
class MissionAdmin(admin.ModelAdmin):
    """Admin configuration for the Mission model."""
    list_display = ('name', 'status', 'description', 'launch_date')  # Fields displayed in list view
    list_filter = ('status', 'launch_date')  # Filters for status & launch_date
    search_fields = ('commander__name',)  # Enable search by commander's name
    readonly_fields = ('updated_at',)  # Make updated_at field read-only

