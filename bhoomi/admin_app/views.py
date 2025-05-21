from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth import logout
from django.shortcuts import render, redirect
from django.views.generic import TemplateView

# Custom test function to check if user is admin
def is_admin(user):
    return user.is_authenticated and user.is_staff  # or user.is_superuser

def unauthorized(request):
    return render(request, 'admin_app/unauthorized.html')

@login_required(login_url='admin_app:unauthorized')  # Redirect to unauthorized page if not logged in
def dashboard(request):
    return render(request, 'admin_app/dashboard.html')

def admin_logout(request):
    logout(request)
    return redirect('admin_app:admin_login')  # Redirect to the admin login page

class AdminLoginView(TemplateView):
    template_name = "admin_app/admin_login.html"
