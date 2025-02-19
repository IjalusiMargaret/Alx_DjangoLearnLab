from django.shortcuts import render
#from django.views.generic import DetailView
from .models import Book
from .models import Library
from django.views.generic.detail import DetailView
from django.shortcuts import  redirect
from django.contrib.auth import login
from django.contrib.auth import logout
from django.contrib.auth import authenticate
from django.contrib.auth.forms import AuthenticationForm 
from django.contrib.auth.forms import UserCreationForm

def user_login(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect("home")  # Change "home" to your desired redirect view
    else:
        form = AuthenticationForm()
    return render(request, "relationship_app/login.html", {"form": form})

def user_logout(request):
    logout(request)
    return render(request, "relationship_app/logout.html")

def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("home")  # Change "home" to your desired redirect view
    else:
        form = UserCreationForm()
    return render(request, "relationship_app/register.html", {"form": form})


def list_books(request):
    books = Book.objects.all()
    return render(request, "relationship_app/list_books.html", {"books": books})


class LibraryDetailView(DetailView):
    model = Library
    template_name = "relationship_app/library_detail.html"
    context_object_name = "library"