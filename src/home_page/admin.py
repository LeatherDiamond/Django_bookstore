from catalog.models import AppUser

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from .forms import MyUserCreationForm, UserChangeForm


class UserAdmin(BaseUserAdmin):
    form = UserChangeForm
    add_form = MyUserCreationForm
    list_display = ("username", "email", "name", "surname", "phone")
    fieldsets = (
        (
            None,
            {
                "fields": (
                    "username",
                    "email",
                    "name",
                    "surname",
                    "phone",
                    "country",
                    "city",
                    "index",
                    "address",
                    "reserve_address",
                    "password",
                    "additional_info",
                )
            },
        ),
        ("Status", {"fields": ("is_staff", "is_superuser", "is_active")}),
        ("Permissions", {"fields": ("groups", "user_permissions")}),
    )

    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": (
                    "username",
                    "email",
                    "name",
                    "surname",
                    "phone",
                    "country",
                    "city",
                    "index",
                    "address",
                    "reserve_address",
                    "password1",
                    "password2",
                    "additional_info",
                ),
            },
        ),
    )
    search_fields = ("username",)
    ordering = ("username",)
    filter_horizontal = ()


admin.site.register(AppUser, UserAdmin)
