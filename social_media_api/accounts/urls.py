from django.urls import path
from .views import RegisterView, CustomAuthToken, ProfileView

urlpatterns = [
    path('register', RegisterView.as_view(), name='register'),  # EXACT match
    path('login', CustomAuthToken.as_view(), name='login'),     # EXACT match
    path('profile', ProfileView.as_view(), name='profile'),     # EXACT match
]
