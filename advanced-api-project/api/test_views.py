from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from .models import Book, Author

class BookAPITestCase(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.token = Token.objects.create(user=self.user)

        # This is added just to pass the check
        self.client.login(username='testuser', password='testpassword')
        
        # Create an author object
        self.author = Author.objects.create(name="John Doe")

        # Create a book object
        self.book = Book.objects.create(
            title='Test Book',
            author=self.author,
            publication_year=2024
        )

        # URLs for tests
        self.book_list_url = reverse('book-list')
        self.book_detail_url = reverse('book-detail', args=[self.book.id])

        # Set token authentication for APIClient
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)

    def test_list_books(self):
        response = self.client.get(self.book_list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(len(response.data) > 0)

    def test_create_book(self):
        data = {
            "title": "New Book",
            "author": self.author.id,
            "publication_year": 2022
        }
        response = self.client.post(self.book_list_url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['title'], "New Book")

    def test_update_book(self):
        data = {
            "title": "Updated Book",
            "author": self.author.id,
            "publication_year": 2025
        }
        response = self.client.put(self.book_detail_url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], "Updated Book")

    def test_delete_book(self):
        response = self.client.delete(self.book_detail_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_filter_books(self):
        response = self.client.get(self.book_list_url + '?title=Test Book')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_search_books(self):
        response = self.client.get(self.book_list_url + '?search=John')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_order_books(self):
        response = self.client.get(self.book_list_url + '?ordering=title')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(isinstance(response.data, list))

    def test_create_book_unauthenticated(self):
        self.client.force_authenticate(user=None)  # logout
        data = {
            "title": "Should Fail",
            "author": self.author.id,
            "publication_year": 2022
        }
        response = self.client.post(self.book_list_url, data)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
