from django.db import models
#from datetime import date

class Author(models.Model):
    """
    Author model to store author's name.
    Each author can have multiple books (One-to-Many relationship).
    """
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Book(models.Model):
    """
    Book model to store book details.
    Each book belongs to one author.
    """
    title = models.CharField(max_length=200)
    publication_year = models.IntegerField()
    author = models.ForeignKey(Author, related_name='books', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.title} ({self.publication_year})"
