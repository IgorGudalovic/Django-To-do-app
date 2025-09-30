from django.urls import path
from . import views

urlpatterns = [
    path('list/',views.list_todos_items),
    path('insert_todo/',views.insert_todo_item, name='insert_todo_item'),
    path('delete_todo/<int:todo_id>/', views.delete_todo_item, name='delete_todo_item'),
    path('toggle_todo/<int:todo_id>/', views.toggle_todo_item, name='toggle_todo_item'),
]