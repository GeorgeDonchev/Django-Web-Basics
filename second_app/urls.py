from django.urls import path

from second_app import views

urlpatterns = [
    path('', views.index, name = 'secondary_index'),
    path('create/', views.create_book, name = 'create_book'),
    path('edit/<int:pk>', views.edit_book, name = 'edit_book'),
    path('delete/<int:pk>', views.delete_book, name = 'delete_book')
]