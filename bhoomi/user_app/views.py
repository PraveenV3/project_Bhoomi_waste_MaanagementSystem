from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from .forms import SignUpForm, ProfileUpdateForm
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.models import User
from .models import UserProfile

def home(request):
    return render(request, 'users/home.html')

# Optionally log the user in right after registration:
def create_and_login_user(request, form):
    user = form.save()
    username = form.cleaned_data.get('username')
    raw_password = form.cleaned_data.get('password1')
    user = authenticate(username=username, password=raw_password)
    login(request, user)
    return user

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            create_and_login_user(request, form)
            return redirect('profile')
    else:
        form = SignUpForm()
    return render(request, 'registration/signup.html', {'form': form})

@login_required
def profile(request):
    user = request.user
    try:
        profile = user.userprofile
    except:
        profile = None
    return render(request, 'users/profile.html', {'user': user, 'profile': profile})

@login_required
def update_profile(request):
    if request.method == 'POST':
        form = ProfileUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = ProfileUpdateForm(instance=request.user)
    return render(request, 'users/update_profile.html', {'form': form})

@login_required
def delete_profile(request):
    if request.method == 'POST':
        request.user.delete()
        logout(request)
        return redirect('signup')
    return render(request, 'users/confirm_delete.html')

@login_required
def bin_manager(request):
    return render(request, 'users/bin_manager.html')

def risk_alerts(request):
    return render(request, 'users/risk_alerts.html')

@login_required
def eco_cleanup(request):
    user = request.user
    try:
        profile = user.userprofile
    except UserProfile.DoesNotExist:
        profile = None
    return render(request, 'users/eco_cleanup.html', {'profile': profile})

@login_required
def collector_profile(request):
    return render(request, 'users/game/collector_profile.html')

# Define a custom decorator to check for superuser status.
def superuser_required(view_func):
    return login_required(user_passes_test(lambda u: u.is_superuser)(view_func))

# View for admin dashboard
@superuser_required
def admin_dashboard(request):
    users = User.objects.all()
    return render(request, 'admin/admin_dashboard.html', {'users': users})

@login_required
def game_ui(request):
    user = request.user
    try:
        profile = user.userprofile
        points = profile.points
        level = 1 + points // 50
    except Exception:
        points = 0
        level = 1
    return render(request, 'users/game/game_ui.html', {'points': points, 'level': level})

@login_required
def report_page(request):
    return render(request, 'users/game/report.html')
