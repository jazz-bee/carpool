from django.contrib import admin
from . import models


# decorator to "register a model" so it's available in the admin page


@admin.register(models.HovLane)
class HovLane(admin.ModelAdmin):
    """manage HovLanes in Django admin"""
    list_display = ('name', 'is_enabled', 'created_at', 'updated_at')

    # pagination
    list_per_page = 5

    # name = models.CharField(max_length=100)
    # is_enabled = models.BooleanField(default=True)
    # created_at = models.DateTimeField(auto_now_add=True)
    # updated_at = models.DateTimeField(auto_now=True)


@admin.register(models.HovMilestone)
class HovMilestone(admin.ModelAdmin):
    pass
