from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BookViewSet
from rest_framework.authtoken.views import obtain_auth_token  

# Create a router and register the BookViewSet
router = DefaultRouter()
router.register(r'books_all', BookViewSet, basename='book_all')

urlpatterns = [
    # Include the router's URLs for CRUD operations on the Book model
    path('', include(router.urls)),
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'), 
]


