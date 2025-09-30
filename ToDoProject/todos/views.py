from django.shortcuts import render, redirect
from django.http import HttpRequest
from django import template
from django.template.defaulttags import register
from .models import ToDo

# Create your views here.
def list_todos_items(request):
    context = {'todo_list': ToDo.objects.all()}
    return render(request, 'todos/todo_list.html', context)

def insert_todo_item(request:HttpRequest):
    todo = ToDo(title = request.POST["content"])
    todo.save()
    return redirect('/todos/list/')

def delete_todo_item(request, todo_id):
    todo = ToDo.objects.get(id=todo_id)
    todo.delete()
    return redirect('/todos/list/')

def toggle_todo_item(request, todo_id):
    todo = ToDo.objects.get(id=todo_id)
    todo.completed = not todo.completed
    todo.save()
    return redirect('/todos/list/')
