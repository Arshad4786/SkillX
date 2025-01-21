from django.contrib import admin
from .models import Talent

@admin.register(Talent)
class TalentAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'approved')  # Display these fields in the admin panel
    list_filter = ('approved',)  # Filter by approval status
    search_fields = ('name', 'email', 'skills')  # Search functionality
