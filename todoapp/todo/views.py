from django.shortcuts import render, redirect
from .models import Todo
# Create your views here.
def HomeView(request):
    todo_list = Todo.objects.all().order_by("-add_date")
    return render(request, 'index.html', {
        "todo_list" : todo_list
    })

def AddTodo(request):
    todo_item = request.POST['todo_item']
    Todo.objects.create(text=todo_item)
    return redirect('home')

def DeleteTodoView(request, todo_id_num):
    get_todo_item = Todo.objects.get(id=todo_id_num)
    # Deleting todo_item
    get_todo_item.delete()
    return redirect('home')
