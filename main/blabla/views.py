import json
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.views.decorators.http import require_POST, require_http_methods


@csrf_exempt
def my_view(request):
    users = UserProfile.objects.all()
    return JsonResponse({"count": users.count()})
    #return HttpResponse("Hello this is my view page")

#Signup view
@csrf_exempt
def signup_view(request):
    if request.method != "POST":
        return JsonResponse({"message": "Only POST method is allowed"}, status=405)

    try:
        data = json.loads(request.body)

        username = data.get("username")
        email = data.get("email")
        password = data.get("password")

        if not username or not password:
            return JsonResponse({"message": "Username or password required"}, status=400)

        if User.objects.filter(username=username).exists():
            return JsonResponse({"message": "User already exists"}, status=409)

        user = User.objects.create_user(
            username=username,
            email=email,
            password=password
        )

        return JsonResponse(
            {
                "message": "User created successfully",
                "username": user.username
            },
            status=201
        )

    except json.JSONDecodeError:
        return JsonResponse({"message": "Invalid JSON"}, status=400)
    except Exception as e:
        return JsonResponse({"message": str(e)}, status=500)

#Login view
@csrf_exempt
def login_view(request):
    if request.method != "POST":
        return JsonResponse({"message": "Only POST method is allowed for login"}, status=405)

    try:
        data = json.loads(request.body)

        username = data.get("username")
        password = data.get("password")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return JsonResponse({"message": f"Login successful! Welcome {user.username}"}, status=200)
        else:
            return JsonResponse({"message": "Invalid username or password"}, status=401)

    except json.JSONDecodeError:
        return JsonResponse({"message": "Invalid JSON"}, status=400)


#Logout view
@csrf_exempt
@require_POST
def logout_view(request):
    if not request.user.is_authenticated:
        return JsonResponse({"message": "User is not authenticated"}, status=401)

    logout(request)
    return JsonResponse({"message": "Logout Successfully"}, status=200)


#Delete View
@csrf_exempt
@require_http_methods(["DELETE"])
def delete_view(request):
    try:
        data = json.loads(request.body)

        username = data.get("username")
        password = data.get("password")
        
        if not username or not password:
            return JsonResponse({"message": "Username or password required"}, status=400)

        user = authenticate(request, username=username, password=password)
        
        if user is None:
            return JsonResponse({"message": "Invalid username or password"}, status=401)
        
        user.delete()
        return JsonResponse({"message": "User successfully deleted"}, status=200)
    
    except json.JSONDecodeError:
        return JsonResponse({"message": "Invalid JSON"}, status=400)
    except User.DoesNotExist:
        return JsonResponse({"message": "User not found"}, status=404)
    
    