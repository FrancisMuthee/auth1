# Import necessary modules and models
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import AbstractUser, PermissionsMixin, UserManager as AuthUserManager
from .models import *



User = get_user_model()

# Define a view function for the home page
def home(request):
    return render(request, 'home.html')

# Define a view function for the login page
def login_page(request):
    # Check if the HTTP request method is POST (form submission)
    if request.method == "POST":
        username = request.POST.get('email')  # Assuming 'email' is used as the username
        password = request.POST.get('password')
        
        # Check if a user with the provided username exists
        if not User.objects.filter(email=username).exists():  # Corrected to filter by 'username' since 'email' is being used as such
            # Display an error message if the username does not exist
            messages.error(request, 'Invalid Email')
            return redirect('/login/')
        
        # Authenticate the user with the provided username and password
        user = authenticate(username=username, password=password)  # Corrected to use 'username' instead of 'email'
        
        if user is None:
            # Display an error message if authentication fails (invalid password)
            messages.error(request, "Invalid Password")
            return redirect('/login/')
        else:
            # Log in the user and redirect to the home page upon successful login
            login(request, user)
            return redirect('/')
    
    # Render the login page template (GET request)
    return render(request, 'login.html')

# Define a view function for the registration page
def register_page(request):
    # Check if the HTTP request method is POST (form submission)
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        password = request.POST.get('password')
        
        # Check if a user with the provided username already exists
        if User.objects.filter(email=email).exists():  # Assuming 'email' is unique and used similarly to 'username'
            # Display an information message if the username is taken
            messages.info(request, "Email already taken!")
            return redirect('/register/')
        else:
            # Create a new User object with the provided information
            user = User.objects.create_user(
                username=email,  # Using email as the username
                  # This is redundant if email is used as username unless you've customized the User model
            )
      
            
            # Display an information message indicating successful account creation
            messages.info(request, "Account created Successfully!")
            return redirect('/login/')
    
    # Render the registration page template (GET request)
    return render(request, 'register.html')

@login_required
def pay(request):
    return render(request, 'pay.html')
