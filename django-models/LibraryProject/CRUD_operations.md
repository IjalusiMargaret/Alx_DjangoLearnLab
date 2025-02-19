from bookshelf.models import Book

book = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)
print(book)


<Book: 1984>


book = Book.objects.get(title="1984")
print(f"Title: {book.title}, Author: {book.author}, Year: {book.publication_year}")


Title: 1984, Author: George Orwell, Year: 1949



book.title = "Nineteen Eighty-Four"
book.save()
print(f"Updated Title: {book.title}")


Updated Title: Nineteen Eighty-Four


book.delete()
print("Book deleted successfully")


Book deleted successfully
