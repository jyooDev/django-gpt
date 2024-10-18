from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import ApplicationUser

# Register your models here.
@admin.register(ApplicationUser)
class ApplicationUserAdmin(UserAdmin):
    fieldsets = (
        (
            "Profile", 
            {
                "fields": (
                    "avatar",
                    "username",
                    "password",
                    "first_name",
                    "last_name",
                    "email",
                )
            }
        ),
        (
            "Permissions",
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                ),
            },
        ),
        ("Important dates", {"fields": ("last_login", "date_joined")}),
    )
    list_display = ("username", "first_name", "last_name",  "email")