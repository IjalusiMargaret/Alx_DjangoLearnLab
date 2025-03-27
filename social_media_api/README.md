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


## User Follow & Feed API

### 1. Follow a User
**Endpoint:** `POST /follow/{user_id}/`  
**Authentication:** Token required  
**Response:**  
```json
{ "message": "You are now following username" }
{ "message": "You have unfollowed username" }


[
  {
    "id": 1,
    "author": "username",
    "content": "Post content",
    "created_at": "2025-03-27T12:00:00Z"
  }
]
