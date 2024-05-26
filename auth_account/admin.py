from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import Group
from .models import CustomUser, ProfilePicture


class CustomUserAdmin(BaseUserAdmin):
    list_display = ["id", "email", "first_name", "last_name", "is_admin"]
    list_filter = ["is_admin"]
    list_editable = ["is_admin"]
    list_per_page = 10
    fieldsets = [
        ("Qario User's Credentials", {"fields": ["email", "password"]}),
        ("Personal info", {"fields": ["first_name", "last_name"]}),
        ("Permissions", {"fields": ["is_admin"]}),
    ]
    add_fieldsets = [
        (
            None,
            {
                "classes": ["wide"],
                "fields": [
                    "email",
                    "first_name",
                    "last_name",
                    "password1",
                    "password2",
                ],
            },
        ),
    ]
    search_fields = ["first_name__startswith", "last_name__startswith", "email"]
    ordering = ["id", "first_name", "last_name"]
    filter_horizontal = []
