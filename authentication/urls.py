
from django.urls import path
from .views import *
# Specify a namespace
app_name="authentication"

urlpatterns = [
    path('users/', RegistrationAPIView.as_view(), name='user-registration'),
    path('users/login/', LoginAPIView.as_view(), name='user_login'),
    path('users/logout/', LogoutView.as_view(), name='use_logout')
]