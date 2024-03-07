from django.shortcuts import render,redirect
from .models import Profile
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User


def profiles(request):
    profiles = Profile.objects.all()
    context = {'profiles': profiles}
    return render(request, 'users/profiles.html', context)


def userProfile(request, pk):
    profile = Profile.objects.get(id=pk)
    topSkills = profile.skill_set.exclude(description__exact='')
    otherSkills = profile.skill_set.filter(description='')
    context = {'profile': profile,'topSkills': topSkills,'otherSkills': otherSkills}
    return render(request, 'users/user-profile.html', context)


# Authentication

def loginUser(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "You are successfully logged in")  # Add error message
            return redirect('profiles')
        else:
            messages.error(request, "Invalid username or password. Please try again.")  # Add error message
            return redirect('login')
    else:
        return render(request, 'users/login_register.html')


def logoutUser(request):
    logout(request)
    messages.success(request, "You have been logged out successfully.")  # Add success message
    return redirect('profiles')


def registerUser(request):
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']  # Use 'password1' field
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, "You have been registered and logged in successfully.")  # Add success message
            return redirect('profiles')
        else:
            messages.error(request, "Error in registration. Please check the form and try again.")  # Add error message
    context = {'form': form}
    return render(request, 'users/login_register.html', context)
