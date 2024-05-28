from django.urls import path
from .views import (
    UserSignupView,
    UserLoginView,
    CustomPasswordResetView,
    UserPasswordResetView,
    SendPasswordResetEmailView,
    LogoutView,
    UserProfileView,
    ProfilePictureView,
    TokenValidationView,
    StudentProfileView,
    TeacherProfileView,
    AllTeachersView,
    AllTeacherImagesView,
)
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path("register/", UserSignupView.as_view(), name="user_signup"),
    path("login/", UserLoginView.as_view(), name="user_login"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path(
        "password/reset/",
        CustomPasswordResetView.as_view(),
        name="custom_password_reset",
    ),
    path(
        "password/reset/confirm/<str:uidb64>/<str:token>/",
        UserPasswordResetView.as_view(),
        name="password_reset_confirm",
    ),
    path(
        "password/reset/send-email/",
        SendPasswordResetEmailView.as_view(),
        name="send_password_reset_email",
    ),
    path("profile/", UserProfileView.as_view(), name="profile"),
    path("profile/picture/", ProfilePictureView.as_view(), name="profile_picture"),
    path("validate/token/", TokenValidationView.as_view(), name="validate_token"),
    path("student/profile/", StudentProfileView.as_view(), name="student_profile"),
    path("teacher/profile/", TeacherProfileView.as_view(), name="teacher_profile"),
    path("teachers/", AllTeachersView.as_view(), name="all_teachers"),
    path("teacher-images/", AllTeacherImagesView.as_view(), name="all_teacher_images"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
