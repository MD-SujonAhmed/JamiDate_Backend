from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Account

class AccountAdmin(UserAdmin):
    model = Account
    list_display = ('Email', 'FirstName', 'LastName', 'is_staff', 'is_active')
    list_filter = ('is_staff', 'is_active')
    fieldsets = (
        (None, {'fields': ('Email', 'password')}),
        ('Personal Info', {'fields': ('FirstName', 'LastName')}),
        ('Permissions', {'fields': ('is_staff', 'is_active', 'is_superuser', 'groups', 'user_permissions')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('Email', 'FirstName', 'LastName', 'password1', 'password2', 'is_staff', 'is_active')}
        ),
    )
    search_fields = ('Email', 'FirstName', 'LastName')
    ordering = ('Email',)

admin.site.register(Account, AccountAdmin)
