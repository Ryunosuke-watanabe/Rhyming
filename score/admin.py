from .models import MyUser
from django.contrib.auth.admin import UserAdmin
from django.contrib import admin
from django.utils.translation import gettext, gettext_lazy as _

# Register your models here.
@admin.register(MyUser)
class AdminUserAdmin(UserAdmin):

    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (_('Personal info'), {'fields': ('full_name', 'email')}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser', 'user_permissions')}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
    list_display = ('username', 'email', 'full_name', 'is_staff')
    search_fields = ('username', 'full_name', 'email')
    filter_horizontal = ('groups', 'user_permissions')

