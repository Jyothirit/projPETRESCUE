from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    # Optionally, customize the display of fields in the admin interface
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('contact','address',)}),
    )

admin.site.register(CustomUser, CustomUserAdmin)
