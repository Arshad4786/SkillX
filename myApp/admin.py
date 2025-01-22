from django.contrib import admin
from .models import Talent, Client, HireRequest

@admin.register(Talent)
class TalentAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'approved')
    list_filter = ('approved',)
    search_fields = ('name', 'email', 'skills')

class ClientAdmin(admin.ModelAdmin):
    list_display = ('name', 'email')

@admin.register(HireRequest)
class HireRequestAdmin(admin.ModelAdmin):
    list_display = ('client', 'talent', 'message', 'status', 'created_at')  # Updated fields
    list_filter = ('status', 'talent', 'client')
    search_fields = ('client__name', 'talent__name', 'message')
    ordering = ('-created_at',)  # Order by most recent

    actions = ['approve_requests', 'reject_requests']

    def approve_requests(self, request, queryset):
        queryset.update(status='Approved')
        self.message_user(request, "Selected requests have been approved.")

    def reject_requests(self, request, queryset):
        queryset.update(status='Rejected')
        self.message_user(request, "Selected requests have been rejected.")

    approve_requests.short_description = "Approve selected requests"
    reject_requests.short_description = "Reject selected requests"
