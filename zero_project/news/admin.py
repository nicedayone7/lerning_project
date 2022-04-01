from django.contrib import admin

from .models import Arts, Category


class ArtsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'category',
                    'creating_date', 'changed_date', 'is_published')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'description')
    list_editable = ('is_published',)
    list_filter = ('is_published', 'category')


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')
    search_fields = ('title',)


admin.site.register(Arts, ArtsAdmin)
admin.site.register(Category, CategoryAdmin)
