from django.urls import path
from .views import BookList  # Ensure you import BookList

urlpatterns = [
    path('books/', BookList.as_view(), name='book-list'),  # Using Django's path() function
]
