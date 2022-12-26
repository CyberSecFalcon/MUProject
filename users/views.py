# In the views.py file within your app (users/views.py), create views for handling the signup, login, logout, and profile update processes:

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .form import IndividualSignupForm, CorporateSignupForm, ProfileUpdateForm

def signup(request):
    # Handle the individual signup process
    if request.method == 'POST':
        form = IndividualSignupForm(request.POST)
        if form.is_valid():
            form.save()
            # Redirect the user to the login page
            return redirect('login')
    else:
        form = IndividualSignupForm()
    return render(request, 'users/signup.html', {'form': form})

def corporate_signup(request):
    # Handle the corporate signup process
    if request.method == 'POST':
        form = CorporateSignupForm(request.POST)
        if form.is_valid():
            form.save()
            # Redirect the user to the login page
            return redirect('login')
    else:
        form = CorporateSignupForm()
    return render(request, 'users/corporate_signup.html', {'form': form})

def login(request):
    # Handle the login process
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # Redirect the user to the home page
            return redirect('home')
        else:
            # Display an error message
            error_message = 'Invalid login credentials'
            return render(request, 'users/login.html', {'error_message': error_message})
    else:
        return render(request, 'users/login.html')

def logout(request):
    # Handle the logout process
    logout(request)
    # Redirect the user to the home page
    return redirect('home')

def profile(request):
    # Handle the profile update process
    if request.method == 'POST':
        form = ProfileUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            # Redirect the user to the profile page
            return redirect('profile')
    else:
        form = ProfileUpdateForm(instance=request.user)
    return render(request, 'users/profile.html', {'form': form})
