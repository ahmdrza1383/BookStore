from django.views import generic

from .models import Book


class BookListView(generic.ListView):
    model = Book
    context_object_name = 'books_list'
    queryset = Book.objects.all()
    template_name = 'books/books_list_view.html'


class BookDetailView(generic.DetailView):
    model = Book
    context_object_name = 'book'
    template_name = 'books/book_detail_view.html'


class BookCreateView(generic.CreateView):
    model = Book
    fields = '__all__'
    template_name = 'books/book_create_view.html'
