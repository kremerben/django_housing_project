from django.contrib import admin
from community.models import Building, Apartment, Renter
# Register your models here.

class BuildingAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Name', {
            'fields': ('name',)
        }),
        ('Advanced options', {
            'classes': ('collapse',),
            'fields': ('address', 'floors',)
        }),
    )
    list_display = ('name','address', 'floors')
    list_filter = ('floors',)

admin.site.register(Building, BuildingAdmin)

class ApartmentAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Name', {
            'fields': ('number', 'building')
        }),
        ('Advanced options', {
            'classes': ('collapse',),
            'fields': ('size', 'rooms', 'rent')
        }),
    )
    list_display = ('number', 'building', 'size', 'rooms', 'rent')
    list_filter = ('number','size', 'rooms', 'rent', 'building')

admin.site.register(Apartment, ApartmentAdmin)

class RenterAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Name', {
            'fields': ('name', 'apartment', 'age')
        }),
        ('Advanced options', {
            'classes': ('collapse',),
            'fields': ('complaints',)
        }),
    )
    list_display = ('name', 'apartment', 'age')
    list_filter = ('name', 'apartment', 'age')

admin.site.register(Renter, RenterAdmin)
