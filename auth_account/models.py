from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager


class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("The Email field must be set")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self.create_user(email, password, **extra_fields)


class CustomUser(AbstractUser):
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.EmailField(
        verbose_name="email address",
        max_length=255,
        unique=True,
    )
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_student = models.BooleanField(default=False)
    is_teacher = models.BooleanField(default=False)
    bio = models.TextField(blank=True)
    address = models.CharField(max_length=255, blank=True)
    objects = CustomUserManager()
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = [
        "first_name",
        "last_name",
    ]

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        return self.is_admin

    @is_staff.setter
    def is_staff(self, value):
        self.is_admin = value


class ProfilePicture(models.Model):
    custom_user = models.OneToOneField(
        CustomUser, on_delete=models.CASCADE, related_name="profile_picture"
    )
    image = models.ImageField(upload_to="profile/pictures", null=True, blank=True)

    def __str__(self):
        return f"{self.custom_user.email} ProfilePicture"


class StudentProfile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='student_profile')
    enrolled_date = models.DateField()
    teacher = models.ForeignKey('TeacherProfile', on_delete=models.SET_NULL, null=True, related_name='students')
    grade = models.CharField(max_length=10)
    parent_contact = models.CharField(max_length=15, blank=True)

    def __str__(self):
        return f"{self.user.email} StudentProfile"


class TeacherProfile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='teacher_profile')
    subject = models.CharField(max_length=100)
    experience = models.IntegerField()
    qualifications = models.TextField(blank=True)

    def __str__(self):
        return f"{self.user.email} TeacherProfile"
