from django.contrib import admin
from .models import Category, TrainingContent

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ['name']

@admin.register(TrainingContent)
class TrainingContentAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'created_at']
    list_filter = ['category']
    search_fields = ['title', 'description']
    fields = ['title', 'category', 'video_path', 'demo_link', 'description'] 