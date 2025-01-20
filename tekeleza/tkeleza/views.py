from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from .forms import ProfileEditForm

# Render the index page
def my_view(request):
    return render(request, 'tkeleza/index.html')

# Handle user login
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            # Authenticate and log in the user
            user = form.get_user()
            login(request, user)
            messages.success(request, f"Welcome back, {user.username}!")
            return redirect('my_view')  # Redirect to the index view
        else:
            # Display error messages for invalid form
            messages.error(request, "Invalid username or password. Please try again.")
    else:
        # Display the login form for GET requests
        form = AuthenticationForm()
    return render(request, 'tkeleza/login.html', {'form': form})

# Handle user signup
def signup_view(request):
    if request.method == "POST":
        # Retrieve form data
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Validate form inputs
        if not all([first_name, last_name, email, username, password]):
            messages.error(request, "All fields are required.")
            return render(request, 'tkeleza/signup.html')

        # Check for duplicate email or username
        if User.objects.filter(email=email).exists():
            messages.error(request, "Email is already in use.")
            return render(request, 'tkeleza/signup.html')
        if User.objects.filter(username=username).exists():
            messages.error(request, "Username is already taken.")
            return render(request, 'tkeleza/signup.html')

        # Create a new user
        user = User.objects.create_user(
            first_name=first_name,
            last_name=last_name,
            email=email,
            username=username,
            password=password,  # Django's create_user hashes the password automatically
        )
        messages.success(request, "Account created successfully. Please log in.")
        return redirect('login')  # Redirect to login page after successful signup

    return render(request, 'tkeleza/signup.html')  # Render signup template

def profile_view(request):
    return render(request, 'tkeleza/profile.html')

def custom_logout(request):
    logout(request)  # Logs out the user
    return redirect('my_view') 

def edit_profile(request):
    if request.method == 'POST':
        form = ProfileEditForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('profile')  # Redirect to the profile page after saving the changes
    else:
        form = ProfileEditForm(instance=request.user)

    return render(request, 'tkeleza/edit_profile.html', {'form': form})