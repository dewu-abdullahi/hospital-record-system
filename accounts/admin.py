from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

# Register your models here.
class CustomAdmin(UserAdmin):
    model = CustomUser
    list_display = ['role', 'username', 'first_name', 'last_name', 'is_staff']
    search_fields = ['role']

    fieldsets = UserAdmin.fieldsets + (('Additional info', {'fields' : ('role',)},),)
    add_fieldsets = UserAdmin.add_fieldsets + (('additional info', {'fields' : ('role',)},),)
admin.site.register(CustomUser, CustomAdmin)
