from django.urls import path,include
from . import views


urlpatterns = [
   path('',views.index,name='index'),
   path('categorybook/<int:id>',views.index2,name='index2'),
   path('books', views.books,name='books'),
   path('update/<int:id>',views.updates,name='update'),
   path('delete/<int:id>',views.delete,name='delete'),

] 