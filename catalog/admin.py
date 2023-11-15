from django.contrib import admin

from catalog.models import Category, Product, Version


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name',)


@admin.register(Product)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'category', 'is_published',)
    list_filter = ('category',)
    search_fields = ('name', 'description',)


@admin.register(Version)
class VersionAdmin(admin.ModelAdmin):
    list_display = ('product', 'number_version', 'title_version', 'is_active',)
    list_filter = ('number_version',)
    search_fields = ('number_version', 'title_version',)
