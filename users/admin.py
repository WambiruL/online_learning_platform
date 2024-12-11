from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, UserManager  # Import your custom User model

# Create a custom UserAdmin class
class CustomUserAdmin(UserAdmin):
    model = User
    # Define the fields to be displayed in the admin list view
    list_display = ('email', 'role', 'is_active', 'is_staff')
    list_filter = ('role', 'is_staff', 'is_active')
    search_fields = ('email',)
    ordering = ('email',)

    # Define the fields to be displayed when adding a user
    add_fieldsets = (
        (None, {
            'fields': ('email', 'password1', 'password2', 'role', 'is_active', 'is_staff')}
        ),
    )

    # Define the fields to be displayed when editing a user
    fieldsets = (
        (None, {'fields': ('email', 'password', 'role', 'is_active', 'is_staff')}),
    )

    # Make sure the user creation form is used when creating a superuser
    add_form = UserManager

# Register the custom user model with the custom admin
admin.site.register(User, CustomUserAdmin)
