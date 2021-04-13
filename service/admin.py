from django.contrib import admin
from .models import Category,Subcategory

class SubcategoryInline(admin.StackedInline):
    model = Subcategory
    prepopulated_fields = {'slug': ('name',)}
    extra = 7


@admin.register(Category)
class AdminCategory(admin.ModelAdmin):
    list_display = ['name',]
    prepopulated_fields = {'slug':('name',)}
    inlines = [SubcategoryInline]