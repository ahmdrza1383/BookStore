from django.urls import reverse_lazy
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


class BookUpdateView(generic.UpdateView):
    model = Book
    fields = '__all__'
    template_name = 'books/book_update_view.html'


class BookDeleteView(generic.DeleteView):
    model = Book
    template_name = 'books/book_delete_view.html'
    success_url = reverse_lazy('books_list')
