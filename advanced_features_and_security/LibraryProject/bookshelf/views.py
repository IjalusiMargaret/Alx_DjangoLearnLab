'''from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from django.contrib.auth.decorators import permission_required
from django.views.decorators.csrf import csrf_exempt
from .models import Book
import json


@permission_required("bookshelf.can_view", raise_exception=True)
def book_list(request):
    """View to list books."""
    books = Book.objects.all().values("id", "title", "author", "publication_year")
    return JsonResponse(list(books), safe=False)


@csrf_exempt
@permission_required("bookshelf.can_create", raise_exception=True)
def create_book(request):
    """View to create a book."""
    if request.method == "POST":
        data = json.loads(request.body)
        book = Book.objects.create(
            title=data["title"],
            author=data["author"],
            publication_year=data["publication_year"],
        )
        return JsonResponse({"message": "Book created successfully", "book_id": book.id})


@csrf_exempt
@permission_required("bookshelf.can_edit", raise_exception=True)
def edit_book(request, book_id):
    """View to edit a book."""
    book = get_object_or_404(Book, id=book_id)

    if request.method == "PUT":
        data = json.loads(request.body)
        book.title = data.get("title", book.title)
        book.author = data.get("author", book.author)
        book.publication_year = data.get("publication_year", book.publication_year)
        book.save()
        return JsonResponse({"message": "Book updated successfully"})


@csrf_exempt
@permission_required("bookshelf.can_delete", raise_exception=True)
def delete_book(request, book_id):
    """View to delete a book."""
    book = get_object_or_404(Book, id=book_id)

    if request.method == "DELETE":
        book.delete()
        return JsonResponse({"message": "Book deleted successfully"})
'''


from django.contrib.auth.decorators import permission_required
from django.http import JsonResponse
from .models import Book

@permission_required('bookshelf.can_view', raise_exception=True)
def view_books(request):
    books = list(Book.objects.values("title", "author", "publication_year"))
    return JsonResponse({"books": books})

@permission_required('bookshelf.can_create', raise_exception=True)
def create_book(request):
    if request.method == "POST":
        title = request.POST.get("title")
        author = request.POST.get("author")
        publication_year = request.POST.get("publication_year")
        book = Book.objects.create(title=title, author=author, publication_year=publication_year)
        return JsonResponse({"message": f"Book '{book.title}' created successfully!"})

@permission_required('bookshelf.can_edit', raise_exception=True)
def edit_book(request, book_id):
    if request.method == "POST":
        book = Book.objects.get(id=book_id)
        book.title = request.POST.get("title", book.title)
        book.author = request.POST.get("author", book.author)
        book.publication_year = request.POST.get("publication_year", book.publication_year)
        book.save()
        return JsonResponse({"message": f"Book '{book.title}' updated successfully!"})

@permission_required('bookshelf.can_delete', raise_exception=True)
def delete_book(request, book_id):
    if request.method == "POST":
        book = Book.objects.get(id=book_id)
        book.delete()
        return JsonResponse({"message": "Book deleted successfully!"})
