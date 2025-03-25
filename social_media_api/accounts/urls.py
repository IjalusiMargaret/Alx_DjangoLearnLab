from django.urls import path
from .views import RegisterView, CustomAuthToken, ProfileView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', CustomAuthToken.as_view(), name='login'),
    path('profile/', ProfileView.as_view(), name='profile'),
]









'''from django.urls import path
from .views import RegisterView, CustomAuthToken, ProfileView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),  # Ensure /register exists
    path('login/', CustomAuthToken.as_view(), name='login'),  # Ensure /login exists
    path('profile/', ProfileView.as_view(), name='profile'),  # Ensure /profile exists
]
'''