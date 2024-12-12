from django.contrib import admin
from .models import Category, News


# Register your models here.
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


@admin.register(News)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'date_posted', 'is_published')
    list_filter = ('category', 'is_published')
    search_fields = ('title', 'content')
    list_per_page = 5

    fieldsets = (
        (None, {
            'fields': ('title', 'content', 'category')
        }),
        ('Дополнительные настройки', {
            'classes': ('collapse',),
            'fields': ('is_published', 'date_posted', 'updated_at')
        }),
    )

    readonly_fields = ('date_posted', 'updated_at')
