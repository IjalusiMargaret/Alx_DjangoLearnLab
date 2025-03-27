# Social Media API

## Endpoints

### Posts
- `GET /api/posts/posts/` → List all posts (paginated)
- `POST /api/posts/posts/` → Create a new post
- `GET /api/posts/posts/<id>/` → Retrieve a specific post
- `PUT /api/posts/posts/<id>/` → Update a post
- `DELETE /api/posts/posts/<id>/` → Delete a post

### Comments
- `GET /api/posts/comments/` → List all comments (paginated)
- `POST /api/posts/comments/` → Create a new comment
- `GET /api/posts/comments/<id>/` → Retrieve a specific comment
- `PUT /api/posts/comments/<id>/` → Update a comment
- `DELETE /api/posts/comments/<id>/` → Delete a comment

### Authentication
- `POST /api/accounts/register/` → Register a user
- `POST /api/accounts/login/` → Login a user (returns token)
- `GET /api/accounts/profile/` → Retrieve user profile
