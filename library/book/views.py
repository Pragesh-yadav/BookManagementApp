from rest_framework import generics
from django.shortcuts import render, redirect
from .models import Book
from .forms import BookCreate
from django.http import HttpResponse, HttpResponseRedirect

from getpass import getpass

from .serializers import bookSerializer


class getAllBooks(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = bookSerializer


class editBookByIdAPI(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = bookSerializer


def loginBookUser(request):
    return getBookforLoggedInUser(request)


def index(request):
    shelf = Book.objects.all()
    return render(request, 'library.html', {'shelf': shelf})


def getBookforLoggedInUser(request):
    shelf = Book.objects.all()
    print(shelf)
    return render(request, 'BookDashboard.html', {'shelf': shelf})


def logout(request):
    return render(request, 'loginBookUser.html')


def addNewBook(request):
    addnewBookRecord = BookCreate()
    return render(request, 'addNewBook.html')
    # if request.method == 'POST':
    #     print("usr is" + getpass.getuser())
    #     if addnewBookRecord.is_valid():
    #         addnewBookRecord.save()
    #     return getBookforLoggedInUser(request)
    # else:
    #     return render(request, '.html', {'upload_form': addnewBookRecord})

def addNewBookData(request):
    print("add new book record view is called")
    addNewBookData = BookCreate()
    if request.method == 'POST':
        addNewBookData= BookCreate(request.POST)
        if addNewBookData.is_valid():

            #data = request.POST.copy()

            #print(data)
            
            addNewBookData.save()
        return getBookforLoggedInUser(request)
   

def editBookById(request, book_id):
    book_id = int(book_id)
    try:
        book_sel = Book.objects.get(id=book_id)
        print("book data is ")
        print(book_sel.id)
    except Book.DoesNotExist:
        redirect('getBookforLoggedInUser/')
       # getBookforLoggedInUser(request)

    return render(request, 'editBook.html', {'shelf': book_sel})


def updateBookById(request, book_id):
    print("upate id called")
    book_id = int(book_id)
    try:
        book_sel = Book.objects.get(id=book_id)
    except Book.DoesNotExist:
        return getBookforLoggedInUser(request)
    book_form = BookCreate(request.POST or None, instance=book_sel)
    if book_form.is_valid():
        book_form.save()
        return getBookforLoggedInUser(request)


def update_book(request, book_id):
    book_id = int(book_id)
    try:
        book_sel = Book.objects.get(id=book_id)
    except Book.DoesNotExist:
        return redirect('index')
    book_form = BookCreate(request.POST or None, instance=book_sel)
    if book_form.is_valid():
        book_form.save()
        return redirect('index')
    return render(request, 'upload_form.html', {'upload_form': book_form})


def delete_book(request, book_id):
    book_id = int(book_id)
    try:
        book_sel = Book.objects.get(id=book_id)
    except Book.DoesNotExist:
        return redirect('index')
    book_sel.delete()
    # response = HttpResponse(status=200)
    # response['Location'] = '/getBookforLoggedInUser/'
    # return response
    return getBookforLoggedInUser(request)
    #return redirect('index')
    #return HttpResponseRedirect(self.request.path_info)
