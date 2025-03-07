import os
import django

# Setup Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_models.settings')
django.setup()

from .models import Author, Book, Library, Librarian

def get_books_by_author(author_name):
    """Query all books written by a specific author."""
    try:
        author = Author.objects.get(name=author_name)
        books = Book.objects.filter(author=author)
        return [book.title for book in books]
    except Author.DoesNotExist:
        return f"No author found with the name '{author_name}'"

def list_books_in_library(library_name):
    """List all books available in a specific library."""
    try:
        library = Library.objects.get(name=library_name)
        books = library.books.all()
        return [book.title for book in books]
    except Library.DoesNotExist:
        return f"No library found with the name '{library_name}'"

def get_librarian_for_library(library_name):
    """Retrieve the librarian associated with a given library."""
    try:
        library = Library.objects.get(name=library_name)
        librarian = Librarian.objects.get(library=library)
        return librarian.name
    except Library.DoesNotExist:
        return f"No library found with the name '{library_name}'"
    except Librarian.DoesNotExist:
        return f"No librarian assigned to the library '{library_name}'"

# Example Usage:
if __name__ == "__main__":
    print("Books by Author John Doe:", get_books_by_author("John Doe"))
    print("Books in Central Library:", list_books_in_library("Central Library"))
    print("Librarian of Central Library:", get_librarian_for_library("Central Library"))
