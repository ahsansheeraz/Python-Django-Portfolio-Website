from django.contrib import admin
from .models import Project

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display =("title", "created_at", "updated_at", "slug")
    prepopulated_fields = {"slug": ("title",)}
    search_fields = ("title", "discription")
    list_filter = ("created_at",)

    def image_preview(self, obj):
        if obj.image:
            return mark_safe(f'<img src="{obj.image.url}" width="80" style="border-radius:6px;" />')
        return "No Image"
