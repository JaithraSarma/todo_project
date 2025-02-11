from django.urls import path
from .views import home, register, user_login, user_logout, create_todo, get_todos, update_todo, delete_todo

urlpatterns = [
    path("", home, name="home"),  
    path("register/", register, name="register"),
    path("login/", user_login, name="login"),
    path("logout/", user_logout, name="logout"),
    path("todos/", get_todos, name="get_todos"),
    path("todos/create/", create_todo, name="create_todo"),
    path("todos/update/<int:todo_id>/", update_todo, name="update_todo"),
    path("todos/delete/<int:todo_id>/", delete_todo, name="delete_todo"),
    path("api/todos/", get_todos, name="get_todos"),
    path("api/todos/create/", create_todo, name="create_todo"),
    path("api/todos/update/<int:todo_id>/", update_todo, name="update_todo"),
    path("api/todos/delete/<int:todo_id>/", delete_todo, name="delete_todo"),
]
