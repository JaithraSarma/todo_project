from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import Todo

# Home Page
@login_required
def home(request):
    todos = Todo.objects.filter(user=request.user)  
    return render(request, "home.html", {"todos": todos})

# User Registration
@csrf_exempt
def register(request):
    if request.method == "POST":
        data = json.loads(request.body)
        username = data.get("username")
        password = data.get("password")
        if User.objects.filter(username=username).exists():
            return JsonResponse({"error": "Username already exists"}, status=400)
        user = User.objects.create_user(username=username, password=password)
        return JsonResponse({"message": "User registered successfully!"}, status=201)

# User Login
@csrf_exempt
def user_login(request):
    if request.method == "POST":
        data = json.loads(request.body)
        username = data.get("username")
        password = data.get("password")
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            return JsonResponse({"message": "Login successful!"}, status=200)
        return JsonResponse({"error": "Invalid credentials"}, status=400)

# User Logout
def user_logout(request):
    logout(request)
    return JsonResponse({"message": "Logged out successfully!"}, status=200)

# API: Create To-Do
@csrf_exempt
@login_required
def create_todo(request):
    if request.method == "POST":
        data = json.loads(request.body)
        todo = Todo.objects.create(
            user=request.user,
            title=data["title"],
            description=data.get("description", "")
        )
        return JsonResponse({"message": "To-Do created!", "todo_id": todo.id}, status=201)

# API: Fetch To-Do List in JSON Format
@login_required
def get_todos(request):
    todos = Todo.objects.filter(user=request.user)
    return JsonResponse({"todos": list(todos.values("id", "title", "description", "is_completed", "created_at"))}, status=200)

# API: Update To-Do
@csrf_exempt
@login_required
def update_todo(request, todo_id):
    if request.method == "PUT":
        data = json.loads(request.body)
        todo = Todo.objects.filter(id=todo_id, user=request.user).update(
            title=data["title"],
            description=data["description"],
            is_completed=data["is_completed"]
        )
        return JsonResponse({"message": "To-Do updated!"}, status=200)

# API: Delete To-Do
@csrf_exempt
@login_required
def delete_todo(request, todo_id):
    if request.method == "DELETE":
        Todo.objects.filter(id=todo_id, user=request.user).delete()
        return JsonResponse({"message": "To-Do deleted!"}, status=200)
