from django.contrib import admin
from rango.models import Category, Page

class PageAdmin(admin.ModelAdmin):
    '''Page Admin'''
    list_display = ('title', 'category', 'url', 'views')

# Register your models here.
admin.site.register(Category)
admin.site.register(Page, PageAdmin)