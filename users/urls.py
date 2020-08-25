from django.urls import path
from .views import UserRegisterView, UserEditView, PasswordsChangeView
from . import views

urlpatterns = [
    path('register/', UserRegisterView.as_view(), name='register'),
    path('edit_profile/', UserEditView.as_view(), name='edit_profile'),
    path('password/', PasswordsChangeView.as_view(template_name='registration/change_password.html')),
    path('password_succes', views.password_succes, name='password_succes'),
]
