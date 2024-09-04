from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView


def home(request):
    return render(request, 'Book/home.html')

def about(request):
    return render(request, 'Book/about.html')

def contact(request):
    return render(request, 'Book/contact.html')

@login_required
def books(request):
    books = Book.objects.all()
    return render(request, 'Book/book.html',{'books': books})
@login_required
def book_detail(request, id):
    book = Book.objects.get(id=id)
    return render(request, 'Book/detail.html',{'book': book})



def signup(request):
    error_message = ''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('books')
        else:
            error_message = 'invalid credentials'
    form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form':form, 'error':error_message})


class Home(LoginView):
    template_name = 'Book/home.html'

class bookCreate(LoginRequiredMixin,CreateView):
    model = Book
    fields = ['title', 'author', 'price', 'category', 'published_date', 'is_bestseller', 'tags']
    template_name = 'Book/createBook.html'
    success_url = '/books/'


class bookUpdate(LoginRequiredMixin,UpdateView):
    model = Book
    fields = ['title', 'author', 'price', 'category', 'published_date', 'is_bestseller', 'tags']
    template_name = 'Book/updateBook.html'
    success_url = '/books/'

class bookDelete(LoginRequiredMixin,DeleteView):
    model = Book
    template_name = 'Book/delete.html'
    success_url = '/books/'



