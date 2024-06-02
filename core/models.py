from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    """
    Custom user model to extend Django's built-in User model.
    You can add custom fields and methods as needed.
    """

    # Add custom fields here if necessary

    # Add related_name to avoid clashes
    groups = models.ManyToManyField(
        "auth.Group",
        related_name="custom_users",
        blank=True,
        verbose_name="groups",
        help_text="The groups this user belongs to. A user will get all permissions granted to each of their groups.",
    )
    user_permissions = models.ManyToManyField(
        "auth.Permission",
        related_name="custom_users",
        blank=True,
        verbose_name="user permissions",
        help_text="Specific permissions for this user.",
        related_query_name="custom_user",
    )


class UserProfile(models.Model):
    """
    Model to store additional information about users.
    """

    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    # Add additional fields like address, contact info, etc.
    email = models.EmailField(max_length=50)
    address = models.CharField(max_length=255)
    contact_number = models.CharField(max_length=20)

    def __str__(self):
        return self.user.username
