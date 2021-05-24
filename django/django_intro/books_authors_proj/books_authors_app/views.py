from typing import ContextManager
from django.shortcuts import render, HttpResponse,redirect
from .models import *


def index(request):
    context = { 
    "books" : Book.objects.all(),
    "authors" : authors.objects.all(),
    }
    return render(request,'index.html',context)
def add_book(request):
    b_title = request.POST['book_title']
    b_desc = request.POST['book_desc']
    Book.objects.create(title=b_title,desc=b_desc)
    return redirect('/')
def show_book(request,the_id):
    book_to_Show = Book.objects.get(id=the_id)
    book_authors=book_to_Show.authors.all()
    authors_to_show = authors.objects.all()
    context = { 
        "book_to_get_title" : book_to_Show.title,
        "book_to_get_id" : book_to_Show.id,
        "book_to_get_desc" : book_to_Show.desc,
        "book_to_get_authors" : book_authors,
        "drop_down_authors" :authors_to_show,
        
    }
    
    return render(request,'books.html',context)
def add_book_to_author(request):
    b_id=request.POST['book_id']
    a_id = request.POST['all_authors_menu']
    this_book=Book.objects.get(id=b_id)
    this_author=authors.objects.get(id=a_id)
    this_book.authors.add(this_author)
    return redirect('/books/' + b_id)
    
def add_author_to_book(request):
    a_id=request.POST['author_id']
    b_id = request.POST['all_books_menu']
    this_author=authors.objects.get(id=a_id)
    this_book=Book.objects.get(id=b_id)
    this_author.books.add(this_book)
    return redirect('/authors/' + a_id)

def show_author(request,the_id):
    author_to_Show = authors.objects.get(id=the_id)
    authors_books=author_to_Show.books.all()
    books_to_Show = Book.objects.all()
    context = { 
        "author_to_get_f_name" : author_to_Show.first_name,
        "author_to_get_l_name" : author_to_Show.last_name,
        "author_to_get_notes" : author_to_Show.notes,
        "author_to_get_id" : author_to_Show.id,
        "author_books" : authors_books,
        "drop_down_books" :books_to_Show,
        
    }
    return render(request,'display_author.html',context)
def add_author(request):
    a_first_name = request.POST['f_name']
    a_last_name = request.POST['l_name']
    Notes = request.POST['notes_box']
    authors.objects.create(first_name=a_first_name,last_name=a_last_name,notes=Notes)
    return redirect('/authors')
def display_author(request):
    context = {
        "all_authors" : authors.objects.all()
    }
    return render(request,'authors.html',context)
