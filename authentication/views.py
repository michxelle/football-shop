from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json
from django.utils.html import strip_tags
from django.conf import settings

@csrf_exempt
def register_flutter(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
        except json.JSONDecodeError:
            return JsonResponse({"status": "error", "message": "Invalid JSON format."}, status=400)

        username = strip_tags(data.get('username', '')).strip()
        password = data.get('password', '')
        
        if not username or not password:
            return JsonResponse({"status": "error", "message": "Username and password are required."}, status=400)
        
        if User.objects.filter(username=username).exists():
            return JsonResponse({"status": "error", "message": "Username is already taken."}, status=409)

        try:
            user = User.objects.create_user(username=username, password=password)
            user.save()
            return JsonResponse({"status": "success", "message": "Registration successful! You can now log in."}, status=201)
        except Exception as e:
            return JsonResponse({"status": "error", "message": f"Registration failed. Error: {str(e)}"}, status=500)
            
    return JsonResponse({"status": "error", "message": "Method not allowed."}, status=405)

@csrf_exempt
def login_flutter(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
        except json.JSONDecodeError:
            return JsonResponse({"status": "error", "message": "Invalid JSON format."}, status=400)

        username = data.get('username', '').strip()
        password = data.get('password', '')
        
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return JsonResponse({
                "status": "success", 
                "message": f"Welcome back, {username}!",
                "username": username
            }, status=200)
        else:
            return JsonResponse({"status": "error", "message": "Invalid username or password."}, status=401)
    return JsonResponse({"status": "error", "message": "Method not allowed."}, status=405)


@csrf_exempt
def logout_flutter(request):
    if request.method == 'POST':
        username = request.user.username if request.user.is_authenticated else "Guest"
        
        if request.user.is_authenticated:
            logout(request)
            return JsonResponse({
                "status": "success", 
                "message": "Logged out successfully!",
                "username": username
            }, status=200)
        else:
            return JsonResponse({"status": "error", "message": "No active session to log out."}, status=400)
            
    return JsonResponse({"status": "error", "message": "Method not allowed."}, status=405)