from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser
#from django.contrib import admin
from .models import  Author, Book, Library, Librarian



#admin.site.register(UserProfile) UserProfile,
admin.site.register(Author)
admin.site.register(Book)
admin.site.register(Library)
admin.site.register(Librarian)


class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ('username', 'email', 'date_of_birth', 'is_staff', 'is_active')
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('date_of_birth', 'profile_photo')}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('date_of_birth', 'profile_photo')}),
    )

admin.site.register(CustomUser, CustomUserAdmin)








'''from django.contrib import admin
from .models import UserProfile, Author, Book, Library, Librarian

# Register models in Django Admin
admin.site.register(UserProfile)
admin.site.register(Author)
admin.site.register(Book)
admin.site.register(Library)
admin.site.register(Librarian)
'''