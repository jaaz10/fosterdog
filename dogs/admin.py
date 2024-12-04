from django.contrib import admin
from .models import Dog

@admin.register(Dog)
class DogAdmin(admin.ModelAdmin):
    list_display = ('name', 'breed', 'age', 'gender', 'size', 'needs_foster', 'created_at')
    list_filter = ('needs_foster', 'size', 'gender')
    search_fields = ('name', 'breed', 'description')
    date_hierarchy = 'created_at'
