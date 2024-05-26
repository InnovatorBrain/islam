from django.urls import path
from .views import UserSignupView, UserLoginView, CustomPasswordResetView, UserPasswordResetView, SendPasswordResetEmailView, LogoutView, UserProfileView, ProfilePictureView, TokenValidationView
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path("register/", UserSignupView.as_view(), name="user_signup"),
    path("SignIn/", UserLoginView.as_view(), name="user_login"),
    path('profile-data/', UserProfileView.as_view(), name='profile'),
    path('password_reset/', CustomPasswordResetView.as_view(), name='custom_password_reset'),
    path('send-password-Email/', SendPasswordResetEmailView.as_view(), name='send_password_reset_email'),
    path('reset-password-Email/<str:uidb64>/<str:token>/', UserPasswordResetView.as_view(), name='password_reset_confirm'),
    path('profile-picture/', ProfilePictureView.as_view(), name='profile_picture'),
    path('validate-token/', TokenValidationView.as_view(), name='validate_token'),
    path('logout/', LogoutView.as_view(), name='logout'),  

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
