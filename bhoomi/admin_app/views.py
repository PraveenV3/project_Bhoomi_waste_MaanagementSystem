from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth import login, logout, authenticate
from .forms import SignUpForm, ProfileUpdateForm
from django.contrib.auth.models import User

# Optional: To limit access to staff or superusers, you can use one of these decorators.
def staff_required(user):
    return user.is_staff or user.is_superuser

from django.contrib.auth.models import User

@login_required
@user_passes_test(staff_required)
def home(request):
    users = User.objects.all()
    return render(request, 'admin/admin_home.html', {'users': users})

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_staff = True  # Mark user as staff/admin
            user.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('admin_app:admin_home')
    else:
        form = SignUpForm()
    return render(request, 'admin/signup.html', {'form': form})

def signin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None and user.is_staff:
            login(request, user)
            return redirect('admin_app:admin_home')
        else:
            error = "Invalid credentials or not an admin user."
            return render(request, 'admin/login.html', {'error': error})
    return render(request, 'admin/login.html')

@login_required
@user_passes_test(staff_required)
def profile(request):
    return render(request, 'admin/profile.html', {'user': request})

@login_required
@user_passes_test(staff_required)
def update_profile(request):
    if request.method == 'POST':
        form = ProfileUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('admin_app:profile')
    else:
        form = ProfileUpdateForm(instance=request.user)
    return render(request, 'admin/update_profile.html', {'form': form})

@login_required
@user_passes_test(staff_required)
def delete_profile(request):
    if request.method == 'POST':
        request.user.delete()
        logout(request)
        return redirect('admin_app:signup')
    return render(request, 'admin/confirm_delete.html')
