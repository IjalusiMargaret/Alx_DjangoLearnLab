# Django Blog - User Authentication System

## Overview
This document explains the implementation of the user authentication system in the `django_blog` project. The system allows users to register, log in, log out, and manage their profile (update their email).

---

## Views Implemented

### 1. `register_view`
- **Path:** `/register/`
- **Description:** Allows users to create a new account using a custom registration form that includes `username`, `email`, `password1`, and `password2`.
- **Template:** `register.html`
- **CSRF:** Uses `{% csrf_token %}` in the registration form.

### 2. `login_view`
- **Path:** `/login/`
- **Description:** Allows existing users to log into their account using their `username` and `password`.
- **Template:** `login.html`
- **CSRF:** Uses `{% csrf_token %}` in the login form.

### 3. `logout_view`
- **Path:** `/logout/`
- **Description:** Logs out the currently authenticated user and redirects them to the login page.
- **No template needed.**

### 4. `profile_view`
- **Path:** `/profile/`
- **Description:** Allows authenticated users to view their profile (username and email) and update their email address.
- **Template:** `profile.html`
- **CSRF:** Uses `{% csrf_token %}` in the profile update form.

---

## CSRF Protection

All forms used in this system are protected from CSRF (Cross-Site Request Forgery) attacks. Django's `{% csrf_token %}` template tag is included in every form:
- **Register Form** (`register.html`)
- **Login Form** (`login.html`)
- **Profile Update Form** (`profile.html`)

Django automatically validates CSRF tokens on all POST requests, ensuring secure handling of form data.

---

## How to Test the Authentication System

### 1. Registration Flow:
1. Visit `/register/` in your browser.
2. Fill out the registration form with `username`, `email`, `password`, and confirm the password.
3. Submit the form and you will be automatically logged in and redirected to `/profile/`.

### 2. Login Flow:
1. Log out first if already logged in via `/logout/`.
2. Visit `/login/`.
3. Enter the correct `username` and `password`.
4. On successful login, you will be redirected to `/profile/`.

### 3. Logout Flow:
1. While logged in, click the **Logout** link from `/profile/` page.
2. You will be redirected to the login page.

### 4. Profile Update Flow:
1. Log in and visit `/profile/`.
2. Update the email address in the form.
3. Submit the form.
4. Your email will be updated, and you will be redirected to the same `/profile/` page showing the updated email.

---

## Notes:
- Make sure the static CSS file is available at `blog/static/css/styles.css` and linked in your `base.html`.
- All views that require authentication (like `/profile/`) are protected using Django's `@login_required` decorator.
- Passwords are securely hashed using Django's built-in password hasher.

---

## Bonus (Optional Enhancements):
- Extend the User model to include profile pictures or a bio using a OneToOne relation (not required for this task).
- Improve form styling using the provided CSS in `styles.css`.

### Blog Post CRUD Features

- Authenticated users can:
  - Create new posts.
  - Edit or delete their own posts.

- Any user (logged-in or anonymous) can:
  - View the post list and individual post details.

- Permissions:
  - Only the post author can edit or delete their post.
  - Login is required to create posts.

### URL patterns:
- /posts/ : List all posts.
- /posts/new/ : Create a new post (login required).
- /posts/<pk>/ : View a specific post.
- /posts/<pk>/edit/ : Edit post (author only).
- /posts/<pk>/delete/ : Delete post (author only).
