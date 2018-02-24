from django.contrib import admin

from .models import Task


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('description', 'creator', 'status')
    list_filter = ['status']

    fieldsets = (
        (None, {
            'fields': ('description', 'additional_info')
        }),
        ('Availability', {
            'fields': ('status', 'creator')
        }),
    )
