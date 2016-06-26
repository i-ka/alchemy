from django.contrib import admin

from AlchemyCommon.models import Element, Category


# Register your models here.

class ElementAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at', 'is_essential_element')

admin.site.register(Element, ElementAdmin)
admin.site.register(Category)
