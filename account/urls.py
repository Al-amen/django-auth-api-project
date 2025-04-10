from django.urls import path
from account.views import(
    UserRegistrationView, 
    UserLoginView, 
    UserProfileView, 
    UserChangePasswordView, 
    SendPasswordResetEmailView,
    UserPasswordResetView,
) 
urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name='user-registration'),
    path('login/', UserLoginView.as_view(), name='user-login'),
    path('profile/',UserProfileView.as_view(),name='profile'),
    path('change-password/',UserChangePasswordView.as_view(),name='change-password'),
    path('send-reset-password-email/',SendPasswordResetEmailView.as_view(),name='send-reset-password-email'),
    path('reset-password/<uidb64>/<token>/',UserPasswordResetView.as_view(),name='reset-password'),
]
