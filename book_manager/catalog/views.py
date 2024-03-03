
from django.shortcuts import render, redirect, reverse
from django.contrib.auth.decorators import login_required
from catalog.models import Book
from users.forms import BookForm
from users.forms import RegisterForm
from recommendations.models import BookRec
from recommendations.models import books_data, books_df



def home_view(request):
    if request.user.is_authenticated:
        return render(request, 'home.html')
    else:
        return redirect('login')

def register_view(request):
    if request.method == 'GET':
        form = RegisterForm()

    else:
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()

            return redirect(reverse('home'))
    return render(request, 'register.html', {
        'form': form
    })

@login_required
def book_list(request):
    books = Book.objects.all()
    return render(request, 'books/lista_mea.html', {'books': books})


@login_required
def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm()
    return render(request, 'books/add_book.html', {'form': form})


@login_required
def edit_book(request, pk):
    book = Book.objects.get(pk=pk)
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm(instance=book)
    return render(request, 'books/edit_book.html', {'form': form, 'book': book})


@login_required
def delete_book(request, pk):
    Book.objects.get(pk=pk).delete()
    return redirect('book_list')


def book_recommendations(request):

    recommender = BookRec(books_df)
    recommendations = recommender.get_top_books(num=3)

    return render(request, 'books/book_recommendations.html', {'recommendations': recommendations})

