from django.db import models
from django.core.exceptions import ValidationError
from datetime import datetime


class Author(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


"""
    Represents an author with a name.
    The 'name' field stores the author's full name.
    """


class Book(models.Model):
    title = models.CharField(max_length=255)
    publication_year = models.IntegerField()
    author = models.ForeignKey('Author', related_name='books', on_delete=models.CASCADE)

    def clean(self):
        current_year = datetime.now().year
        if self.publication_year > current_year:
            raise ValidationError({"publication_year": "Publication year cannot be in the future."})

    def save(self, *args, **kwargs):
        self.clean()  # Call clean() before saving
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title



"""
This module defines serializers for the API.

BookSerializer:
- Serializes all fields of the Book model.
- Validates that publication_year is not in the future.

AuthorSerializer:
- Includes the author’s name.
- Uses a nested BookSerializer to include related books.
"""
