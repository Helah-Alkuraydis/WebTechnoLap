
from django.http import HttpResponse # type: ignore
from django.shortcuts import render  # type: ignore
from .models import Book, Address, Student, Author, Publisher
from django.db.models import Count, Sum, Avg, Max, Min,Q, F, FloatField, ExpressionWrapper


# def index(request):
#     name = request.GET.get("name") or "world!"
#     return render(request, "bookmodule/index.html")

def index(request):
    name = request.GET.get("name") or "world"
    return render(request, "bookmodule/index.html", {"name": name})

# def index(request):
#     name = request.GET.get("name") or "world!"  
#     return HttpResponse("Hello, "+name)

def index2(request, val1 = 0):
    return HttpResponse("value1 = "+str(val1))


def viewbook(request, bookId):
    # assume that we have the following books somewhere (e.g. database)
    book1 = {'id':123, 'title':'Continuous Delivery', 'author':'J. Humble and D. Farley'}
    book2 = {'id':456, 'title':'Secrets of Reverse Engineering', 'author':'E. Eilam'}
    targetBook = None
    if book1['id'] == bookId: targetBook = book1
    if book2['id'] == bookId: targetBook = book2
    context = {'book':targetBook} # book is the variable name accessible by the template
    return render(request, 'bookmodule/show.html', context)

def index(request):
    return render(request, "bookmodule/index.html")
 
def list_books(request):
    return render(request, 'bookmodule/list_books.html')
 
def viewbook(request, bookId):
    return render(request, 'bookmodule/one_book.html')
 
def aboutus(request):
    return render(request, 'bookmodule/aboutus.html')


def links_page(request):
    return render(request, 'bookmodule/links.html')

def formatting_page(request):
    return render(request, 'bookmodule/formatting.html')

def listing_page(request):
    return render(request, 'bookmodule/listing.html')

def tables_page(request):
    return render(request, 'bookmodule/tables.html')

def __getBooksList():
    book1 = {'id':12344321, 'title':'Continuous Delivery', 'author':'J.Humble and D. Farley'}
    book2 = {'id':56788765,'title':'Reversing: Secrets of Reverse Engineering', 'author':'E. Eilam'}
    book3 = {'id':43211234, 'title':'The Hundred-Page Machine Learning Book', 'author':'Andriy Burkov'}
    return [book1, book2, book3]

def search(request):
    if request.method == "POST":
        string = request.POST.get('keyword').lower()
        isTitle = request.POST.get('option1')
        isAuthor = request.POST.get('option2')
        # now filter
        books = __getBooksList()
        newBooks = []
        for item in books:
            contained = False
            if isTitle and string in item['title'].lower(): contained = True
            if not contained and isAuthor and string in item['author'].lower():contained = True
            
            if contained: newBooks.append(item)
        return render(request, 'bookmodule/bookList.html', {'books':newBooks})
    return render(request, 'bookmodule/search.html')


def insert_book(request):
    mybook = Book(title='Continuous Delivery', author='J.Humble and D. Farley', price= 120.00 , edition=3)
    mybook.save()
    mybook = Book(title='Reversing: Secrets of Reverse Engineer', author='E. Eilam', price= 97.00, edition=2)
    mybook.save()
    mybook = Book(title='The Hundred-Page Machine Learning Book ', author='Andriy Burkov', price= 100.00, edition=4)
    
    mybook.save() 

    mybook = Book.objects.create(title = 'Continuous Delivery 22', author = 'J.Humble and D. Farley', edition = 1)
    mybook.save() 

    return HttpResponse("تم إضافة الكتاب لقاعدة البيانات بنجاح باستخدام كود جانجو! ")


def simple_query(request):
    mybooks = Book.objects.filter(title__icontains='and') 
    return render(request, 'bookmodule/bookList.html', {'books': mybooks})

def complex_query(request):
    mybooks = Book.objects.filter(author__isnull=False).filter(title__icontains='and').filter(edition__gte=2).exclude(price__lte=100)[:10]
    
    if len(mybooks) >= 1:
        return render(request, 'bookmodule/bookList.html', {'books': mybooks})
    else:
        return render(request, 'bookmodule/index.html')
    
# def task1o(request):
#     task1_books = Book.objects.filter(Q(price__lte=80.0))
#     return render(request, 'bookmodule/task1.html', {'books': task1_books})

# def task2o(request):
#     task2_books = Book.objects.filter(
#         Q(edition__gt=3) & (Q(title__icontains='qu') | Q(author__icontains='qu'))
#     )
#     return render(request, 'bookmodule/task2.html', {'books': task2_books})

# def task3o(request):
#     task3_books = Book.objects.filter(
#         ~Q(edition__gt=3) & ~(Q(title__icontains='qu') | Q(author__icontains='qu'))
#     )
#     return render(request, 'bookmodule/task3.html', {'books': task3_books})

# def task4o(request):
#     task4_books = Book.objects.order_by('title')
#     return render(request, 'bookmodule/task4.html', {'books': task4_books})

# def task5o(request):
#     stats = Book.objects.aggregate(
#         my_count=Count('id'),
#         my_sum=Sum('price'),
#         my_avg=Avg('price'),
#         my_max=Max('price'),
#         my_min=Min('price')
#     )
#     return render(request, 'bookmodule/task5.html', {'stats': stats})

# def task7o(request):
#     cities = Address.objects.annotate(student_count=Count('student'))
#     return render(request, 'bookmodule/task7.html', {'cities': cities})

def task1(request):
    total_qty = Book.objects.aggregate(total=Sum('quantity'))['total']

    if total_qty is None:
        total_qty = 1 

    task1_books = Book.objects.annotate(
        percentage=ExpressionWrapper(
            (F('quantity') * 100.0) / total_qty,
            output_field=FloatField()
        )
    )

    return render(request, 'bookmodule/task19.html', {'books': task1_books})

def task2(request):
    publishers = Publisher.objects.annotate(total_stock=Sum('book__quantity'))

    return render(request, 'bookmodule/task29.html', {'publishers': publishers})

def task3(request):
    publishers = Publisher.objects.annotate(oldest_book_date=Min('book__pubdate'))

    return render(request, 'bookmodule/task39.html', {'publishers': publishers})


def task4(request):
    publishers = Publisher.objects.annotate(
        avg_price=Avg('book__price'),
        min_price=Min('book__price'),
        max_price=Max('book__price')
    )
    return render(request, 'bookmodule/task49.html', {'publishers': publishers})


def task5(request):
    publishers = Publisher.objects.annotate(
        high_rated_count=Count('book', filter=Q(book__rating__gte=4)),
        high_rated_quantity=Sum('book__quantity', filter=Q(book__rating__gte=4))
    )
    return render(request, 'bookmodule/task59.html', {'publishers': publishers})

def task6(request):
    publishers = Publisher.objects.annotate(
        target_books_count=Count(
            'book', 
            filter=Q(book__price__gt=50) & Q(book__quantity__lt=5) & Q(book__quantity__gte=1)
        )
    )
    return render(request, 'bookmodule/task6.html', {'publishers': publishers})