from django.contrib import admin
from .models import Talent, Client, HireRequest

@admin.register(Talent)
class TalentAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'approved')  # Display these fields in the admin panel
    list_filter = ('approved',)  # Filter by approval status
    search_fields = ('name', 'email', 'skills')  # Search functionality


class ClientAdmin(admin.ModelAdmin):
    list_display = ('name', 'email')

@admin.register(HireRequest)
class HireRequestAdmin(admin.ModelAdmin):
    list_display = ('client', 'talent', 'status', 'date_sent')
    list_filter = ('status', 'talent', 'client')
    search_fields = ('client__name', 'talent__name', 'message')