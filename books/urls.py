from django.urls import path
from .views import get_info, get_books, detail, add_book, update_book




urlpatterns = [
    path('', get_info, name='get_info'),
    path('book/<int:pk>', get_books, name='get_books'),
    path('books/<int:pk>', detail, name='detail'),
    path('add_book', add_book, name='add_book'),
    path('update/<int:pk>', update_book, name='update'),
]