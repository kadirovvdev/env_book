from django.shortcuts import render, redirect
from .models import Books_category, Books, Author, Book_author, Review
from .forms import BookForm


def get_info(request):
    categorys = Books_category.objects.all()

    context = {
        'category': categorys
    }
    return render(request, 'index.html', context=context)


def get_books(request, pk):
    bookss = Books.objects.filter(pk=pk)
    context = {
        'book': bookss
    }
    return render(request, 'books.html', context=context)

def detail(request, pk):
    books = Books.objects.get(pk=pk)
    context = {
        'book': books
    }
    return render(request, 'detail.html', context=context)


def add_book(request):
    form = BookForm(request.POST, request.FILES)
    if form.is_valid():
        form.save()
        return redirect('get_info')
    context = {
        'form': form
        }
    return render(request, 'create.html', context=context)

def update_book(request, pk):
    data = Books.objects.get(pk=pk)
    form = BookForm(request.POST, request.FILES, instance=data)
    if form.is_valid():
        print(1)
        form.save()
        return redirect('get_info')
    context = {
        'form': form
        }
    return render(request, 'update.html', context=context)

def delete_book(request, pk):
    data = Books.objects.get(pk=pk)
    data.delete()
    return redirect('get_info')


