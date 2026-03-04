from django.urls import path # type: ignore
from . import views

urlpatterns = [
  # path('', views.index),
  # path('index2/<int:val1>/', views.index2),
  # path('<int:bookId>', views.viewbook)
    path('', views.index, name= "books.index"),
    path('list_books/', views.list_books, name= "books.list_books"),
    path('<int:bookId>/', views.viewbook, name="books.view_one_book"),
    path('aboutus/', views.aboutus, name="books.aboutus"),
    path('html5/links/', views.links_page, name='books.links_page'),
    path('html5/text/formatting/', views.formatting_page, name='books.formatting_page'),
    path('html5/listing/', views.listing_page, name='books.listing_page'),
    path('html5/tables/', views.tables_page, name='books.tables_page'),
]
