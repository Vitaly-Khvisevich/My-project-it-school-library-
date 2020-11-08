from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.Main, name='Main'),
    path('New/', views.News, name='New'),
    path('About/', views.About, name='About'),
    path('<int:book_id>/', views.book_id, name = 'Book_id'),
    path('Auth/', views.book_loginView.as_view(), name = 'Auth'),
    path('By_novelty/', views.By_novelty, name = 'By_novelty'),
    path('By_author/', views.By_author, name = 'By_author'),
    path('By_comments/', views.By_comments, name = 'By_comments'),
    path('By_author/<str:author>/', views.id_author, name = 'id_author'),
    path ('Register/', views.book_userView.as_view(), name = 'Register' ),
    path ('Logout/', views.book_logOut.as_view(), name = 'Logout' ),
    path ('Add_book/', views.add_book.as_view(), name = 'add_book'),
    path('add_comment/', views.add_comment, name = 'add_comment')
    
    
]