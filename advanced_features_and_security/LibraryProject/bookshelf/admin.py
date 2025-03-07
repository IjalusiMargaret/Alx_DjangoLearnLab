#from django.contrib import admin
'''from .models import Book
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser  # Import the Book model

# Register Book model
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "publication_year")  # Columns shown in admin list view
    search_fields = ("title", "author")  # Enables search functionality
    list_filter = ("publication_year",)  # Adds a filter for publication year



class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ("username", "email", "date_of_birth", "is_staff", "is_active")
    fieldsets = UserAdmin.fieldsets + (
        (None, {"fields": ("date_of_birth", "profile_photo")}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {"fields": ("date_of_birth", "profile_photo")}),
    )

admin.site.register(CustomUser, CustomUserAdmin)





from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, Book  # Import both models properly

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "publication_year") 
    search_fields = ("title", "author") 
    list_filter = ("publication_year",) 

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ("username", "email", "date_of_birth", "is_staff", "is_active")

    fieldsets = UserAdmin.fieldsets + (
        (None, {"fields": ("date_of_birth", "profile_photo")}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {"fields": ("date_of_birth", "profile_photo")}),
    )

admin.site.register(CustomUser, CustomUserAdmin)
'''


from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from .models import Book
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser  # Import the Book model

# Register Book model
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "publication_year")  # Columns shown in admin list view
    search_fields = ("title", "author")  # Enables search functionality
    list_filter = ("publication_year",)  # Adds a filter for publication year



class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ("username", "email", "date_of_birth", "is_staff", "is_active")
    fieldsets = UserAdmin.fieldsets + (
        (None, {"fields": ("date_of_birth", "profile_photo")}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {"fields": ("date_of_birth", "profile_photo")}),
    )

admin.site.register(CustomUser, CustomUserAdmin)


def create_groups():
    # Get content type for the Book model
    book_content_type = ContentType.objects.get_for_model(Book)

    # Define permissions
    permissions = {
        "can_view": Permission.objects.get(codename="can_view", content_type=book_content_type),
        "can_create": Permission.objects.get(codename="can_create", content_type=book_content_type),
        "can_edit": Permission.objects.get(codename="can_edit", content_type=book_content_type),
        "can_delete": Permission.objects.get(codename="can_delete", content_type=book_content_type),
    }

    # Define and create groups
    groups = {
        "Viewers": ["can_view"],
        "Editors": ["can_view", "can_create", "can_edit"],
        "Admins": ["can_view", "can_create", "can_edit", "can_delete"],
    }

    for group_name, perms in groups.items():
        group, created = Group.objects.get_or_create(name=group_name)
        group.permissions.set([permissions[perm] for perm in perms])

    print("Groups and permissions have been set up.")

