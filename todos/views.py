
from django.shortcuts import render, redirect
from .models import Todo

def index(request):
    todos = Todo.objects.all()
    return render(request, 'todos/index.html', {'todos': todos})

def add_todo(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        if title:
            Todo.objects.create(title=title)
    return redirect('index')

def delete_todo(request, id):
    todo = Todo.objects.get(id=id)
    todo.delete()
    return redirect('index')

def toggle_todo(request, id):
    todo = Todo.objects.get(id=id)
    todo.completed = not todo.completed
    todo.save()
    return redirect('index')
# Create your views here.
