from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import Group
from .models import CustomUser, ProfilePicture, StudentProfile, TeacherProfile

class CustomUserAdmin(BaseUserAdmin):
    list_display = ["id", "email", "first_name", "last_name", "is_admin"]
    list_filter = ["is_admin"]
    list_editable = ["is_admin"]
    list_per_page = 10
    fieldsets = [
        ("CropShield User's Credentials", {"fields": ["email", "password"]}),
        ("Personal Info", {"fields": ["first_name", "last_name"]}),
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

class ProfilePictureAdmin(admin.ModelAdmin):
    list_display = ["id", "custom_user", "image"]
    list_per_page = 10
    search_fields = ["custom_user__email"]

class StudentProfileAdmin(admin.ModelAdmin):
    list_display = ["id", "user_email", "user_first_name", "user_last_name"]
    list_per_page = 10
    search_fields = ["user__email"]

    def user_email(self, obj):
        return obj.user.email
    user_email.short_description = "Email"

    def user_first_name(self, obj):
        return obj.user.first_name
    user_first_name.short_description = "First Name"

    def user_last_name(self, obj):
        return obj.user.last_name
    user_last_name.short_description = "Last Name"

class TeacherProfileAdmin(admin.ModelAdmin):
    list_display = ["id", "user_email", "user_first_name", "user_last_name"]
    list_per_page = 10
    search_fields = ["user__email"]

    def user_email(self, obj):
        return obj.user.email
    user_email.short_description = "Email"

    def user_first_name(self, obj):
        return obj.user.first_name
    user_first_name.short_description = "First Name"

    def user_last_name(self, obj):
        return obj.user.last_name
    user_last_name.short_description = "Last Name"

# Registering the models with their custom admin configurations
admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(ProfilePicture, ProfilePictureAdmin)
admin.site.register(StudentProfile, StudentProfileAdmin)
admin.site.register(TeacherProfile, TeacherProfileAdmin)

admin.site.unregister(Group)
