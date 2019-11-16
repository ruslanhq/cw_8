from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from accounts.views import register_view, UserDetailView, UserChangeView, UserChangePasswordView

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register', register_view, name='register'),
    path('profile/<int:pk>/', UserDetailView.as_view(), name='user_detail'),
    path('profile/edit/<int:pk>/', UserChangeView.as_view(), name='user_edit'),
    path('profile/edit/pass/<int:pk>', UserChangePasswordView.as_view(), name='user_edit_pass'),
]

app_name = 'accounts'
