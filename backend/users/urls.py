from django.urls import path
from .views import UserDetailView, UserRegisterView, ChangePasswordView, UserDeleteAccountView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
urlpatterns = [
    path('profile/', UserDetailView.as_view(), name='user_detail'),
    path('register/', UserRegisterView.as_view(), name='register'),
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('change-password/', ChangePasswordView.as_view(), name='change_password'),
    path('delete-account/', UserDeleteAccountView.as_view(), name='delete_account'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]