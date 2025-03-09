from rest_framework import viewsets
from .models import Book
from .serializers import BookSerializer

# ViewSet for CRUD operations on Book model
class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()  # Fetch all books from database
    serializer_class = BookSerializer  # Use BookSerializer to convert data
