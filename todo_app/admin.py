from django.contrib import admin
from .models import Todo

class TodoAdmin(admin.ModelAdmin):
    list_display = ("title", "user", "is_completed", "created_at")
    list_filter = ("user", "is_completed")
    search_fields = ("title", "user__username")

admin.site.register(Todo, TodoAdmin)
