from django.urls import path     
from . import views

urlpatterns = [
    path('', views.index),
    path('add_book',views.add_book),
    path('add_author',views.add_author),
    path('authors',views.display_author),
    path('authors/<int:the_id>',views.show_author),
    path('books/<int:the_id>',views.show_book),
    path('add_book_to_author',views.add_book_to_author),
    path('add_author_to_book',views. add_author_to_book)

]