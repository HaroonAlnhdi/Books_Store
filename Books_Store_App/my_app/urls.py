from django.urls import path,include
from . import views
urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('books/', views.books, name='books'),
    path('books/<int:id>', views.book_detail, name='detail'),
    path('books/create', views.bookCreate.as_view(), name='create'),
    path('books/update/<int:pk>', views.bookUpdate.as_view(), name='update'),
    path('books/delete/<int:pk>', views.bookDelete.as_view(), name='delete'),
    path('accounts/signup/', views.signup, name='signup'),

]