from django.contrib import admin
from .models import Book  # Import the Book model

# Register Book model
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "publication_year")  # Columns shown in admin list view
    search_fields = ("title", "author")  # Enables search functionality
    list_filter = ("publication_year",)  # Adds a filter for publication year
