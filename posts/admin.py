from django.contrib import admin
from .models import Article

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {
            'fields': ('titel', 'author')
        }),
        ('Important dates', {
            'fields': ('created', 'edited')
        }),
        ('Content', {
            'fields': ('content',)
        })
    ]
    readonly_fields = ('created', 'edited')
    list_display = ('titel', 'author', 'status')
    list_filter = ('status',)
    search_fields = ('titel', 'author__username')