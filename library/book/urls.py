from django.urls import path
from . import views
#from library import DEBUSTATIC_URL, STATIC_ROOT, MEDIA_URL, MEDIA_ROOT
#from django.conf.urls.static import static

urlpatterns = [

    path('', views.getAllBooks.as_view()),
    path('getAllBooks', views.getAllBooks.as_view()),
    path('editBookByIdAPI', views.editBookByIdAPI.as_view()),
    # path('', views.loginBookUser, name = 'loginBookUser'),
    path('loginBookUser/', views.loginBookUser, name='loginBookUser'),
    path('getBookforLoggedInUser/', views.getBookforLoggedInUser,name='getBookforLoggedInUser'),

    path('addNewBook/', views.addNewBook, name='addNewBook'),
    path('addNewBookData/', views.addNewBookData, name='addNewBookData'),

    path('editBookById/<int:book_id>', views.editBookById),
    path('updateBookById/<int:book_id>', views.updateBookById),
    path('logout/', views.logout, name='logout'),
    #path('upload/', views.upload, name = 'upload-book'),
    # path('loginBookUser/update/<int:book_id>', views.editBook),
    path('delete/<int:book_id>', views.delete_book)
]
# DataFlair
'''if DEBUG:
    urlpatterns += static(STATIC_URL, document_root = STATIC_ROOT)
    urlpatterns += static(MEDIA_URL, document_root = MEDIA_ROOT)'''
