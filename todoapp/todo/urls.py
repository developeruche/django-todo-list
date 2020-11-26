from django.urls import path
from .views import HomeView, AddTodo, DeleteTodoView


urlpatterns = [
    path('', HomeView, name="home"),
    path('addtodo/', AddTodo, name="add_todo"),
    path('deletetodo/<int:todo_id_num>/', DeleteTodoView, name="del_todo"),
]
