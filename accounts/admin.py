# Django Imports
from django.contrib import admin

# Own Imports
from accounts.models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'uuid', 'firstname', 'lastname', 'username', 'email', 'is_active', 'is_staff', 'is_superuser', )