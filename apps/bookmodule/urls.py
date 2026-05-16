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
    path('search/', views.search, name='books.search'),
    path('insert/', views.insert_book, name='books.insert'),
    path('simple/query', views.simple_query, name='books.simple_query'),
    path('complex/query', views.complex_query, name='books.complex_query'),
    # path('lab8/task1', views.task1, name='task1'),
    # path('lab8/task2', views.task2, name='task2'),
    # path('lab8/task3', views.task3, name='task3'),
    # path('lab8/task4', views.task4, name='task4'),
    # path('lab8/task5', views.task5, name='task5'),
    # path('lab8/task7', views.task7, name='task7'),
    path('lab9/task1', views.task1, name='lab9.task1'),
    path('lab9/task2', views.task2, name='lab9.task2'),
    path('lab9/task3', views.task3, name='lab9.task3'),
    path('lab9/task4', views.task4, name='lab9.task4'),
    path('lab9/task5', views.task5, name='lab9.task5'),
    path('lab9/task6', views.task6, name='lab9.task6'),
    
    path('lab9_part1/listbooks', views.listbooks, name='lab9_part1.listbooks'),
    path('lab9_part1/addbook', views.addbook, name='lab9_part1.addbook'),
    path('lab9_part1/editbook/<int:id>', views.editbook, name='lab9_part1.editbook'),
    path('lab9_part1/deletebook/<int:id>', views.deletebook, name='lab9_part1.deletebook'),

    path('lab9_part2/listbooks', views.listbooks2, name='lab9_part2.listbooks'),
    path('lab9_part2/addbook', views.addbook2, name='lab9_part2.addbook'),
    path('lab9_part2/editbook/<int:id>', views.editbook2, name='lab9_part2.editbook'),
    path('lab9_part2/deletebook/<int:id>', views.deletebook2, name='lab9_part2.deletebook'),


    # Lap 11

    path('lab11/task1/students', views.list_students, name='list_students'),
    path('lab11/task1/addstudent', views.add_student, name='add_student'),
    path('lab11/task1/editstudent/<int:id>', views.edit_student, name='edit_student'),
    path('lab11/task1/deletestudent/<int:id>', views.delete_student, name='delete_student'),

    path('lab11/task2/students', views.list_students2, name='list_students2'),
    path('lab11/task2/addstudent', views.add_student2, name='add_student2'),
    path('lab11/task2/editstudent/<int:id>', views.edit_student2, name='edit_student2'),
    path('lab11/task2/deletestudent/<int:id>', views.delete_student2, name='delete_student2'),

    path('lab11/task3/documents', views.list_documents, name='list_documents'),
    path('lab11/task3/add_document', views.add_document, name='add_document'),
    path('users/register', views.register_user, name='register_user'),
    path('users/login', views.login_user, name='login_user'),
    path('users/logout', views.logout_user, name='logout_user'),
]
