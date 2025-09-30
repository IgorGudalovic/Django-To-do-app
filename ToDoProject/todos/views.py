from django.shortcuts import render, redirect
from django.http import HttpRequest
from .models import ToDo

# Create your views here.
def list_todos_items(request):
    return render(request, 'todos/todo_list.html')

def insert_todo_item(request:HttpRequest):
    todo = ToDo(title = request.POST["content"])
    todo.save()
    return redirect('/todos/list/')