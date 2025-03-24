from django.urls import path
from .views import RegisterView, CustomAuthToken, ProfileView

urlpatterns = [
    path('register', RegisterView.as_view(), name='register'),  # removed trailing slash
    path('login', CustomAuthToken.as_view(), name='login'),
    path('profile', ProfileView.as_view(), name='profile'),
]
