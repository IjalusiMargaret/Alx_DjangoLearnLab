from django.urls import path
from rest_framework.authtoken.views import ObtainAuthToken
from .views import RegisterView, ProfileView
from .views import FollowUserView, UnfollowUserView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', ObtainAuthToken.as_view(), name='login'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('follow/<int:user_id>/', FollowUserView.as_view(), name='follow-user'),  # Ensures correct format
    path('unfollow/<int:user_id>/', UnfollowUserView.as_view(), name='unfollow-user'),

]


