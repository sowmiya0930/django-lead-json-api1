from django.contrib import admin
from .models import Lead

@admin.register(Lead)
class LeadAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'email', 'status', 'owner', 'created_at')
    search_fields = ('first_name', 'last_name', 'email', 'company')
    list_filter = ('status', 'lead_source')

