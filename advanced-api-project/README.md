Testing Documentation
1. Testing Strategy
The testing strategy for this project follows Django's built-in testing framework using unittest and DRF's APITestCase to validate API functionality. The focus is on:

CRUD Operations for the Book API endpoints.
Ensuring filtering, searching, and ordering work as expected.
Verifying authentication and permissions are correctly enforced.
2. Test Cases Overview
Test Name	Description
test_list_books	Tests the GET /books/ endpoint to retrieve a list of books.
test_create_book	Tests the POST /books/ endpoint to create a new book (requires authentication).
test_update_book	Tests the PUT /books/<id>/ endpoint to update an existing book (requires authentication).
test_delete_book	Tests the DELETE /books/<id>/ endpoint to delete a book (requires authentication).
test_search_books	Tests the search functionality (e.g., GET /books/?search=keyword).
test_filter_books	Tests filtering by title, author, and publication_year (e.g., GET /books/?title=xyz).
test_ordering_books	Tests ordering functionality (e.g., GET /books/?ordering=title).
test_permission_denied_for_anon	Tests that unauthenticated users cannot create, update, or delete books.
3. How to Run the Tests
Navigate to your project directory:

bash
Copy
Edit
cd advanced-api-project
Run the tests using Django’s test runner:

bash
Copy
Edit
python manage.py test api
4. Understanding Test Results
OK: All tests passed successfully.
FAIL: Some tests failed. The error traceback will indicate which assertion failed (e.g., incorrect status code, data mismatch).
Creating test database: Django will automatically create a temporary test database to isolate tests from your development/production data.
5. Notes
Tests that require authentication automatically create a test user and obtain a token for protected endpoints.
Make sure DRF Token Authentication is configured if using token-based access for tests.
Filtering, searching, and ordering are tested using query parameters in the URL.
