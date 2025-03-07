# Django Permissions and Groups

## Overview
This project implements permissions and groups to control access to various parts of the Django application.

## Permissions
The following custom permissions have been added to the `Book` model:
- `can_view`: Can view books
- `can_create`: Can create books
- `can_edit`: Can edit books
- `can_delete`: Can delete books

## Groups
The following groups are set up:
- `Editors`: Can create and edit books.
- `Viewers`: Can only view books.
- `Admins`: Can create, edit, and delete books.

## Testing
To test permissions:
1. Create users and assign them to groups in Django admin or via shell.
2. Log in as different users and attempt different actions.
