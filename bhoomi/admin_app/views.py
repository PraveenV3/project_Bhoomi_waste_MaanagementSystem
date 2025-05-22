from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth import logout, authenticate, login
from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.models import User

# Custom test function to check if user is admin
def is_admin(user):
    return user.is_authenticated and user.is_staff  # or user.is_superuser

def unauthorized(request):
    return render(request, 'admin_app/unauthorized.html')

@login_required(login_url='admin_app:unauthorized')  # Redirect to unauthorized page if not logged in
def dashboard(request):
    total_users = User.objects.count()
    context = {
        'total_users': total_users,
    }
    return render(request, 'admin_app/dashboard.html', context)

def admin_logout(request):
    logout(request)
    return redirect('admin_app:admin_login')  # Redirect to the admin login page

class AdminLoginView(View):
    template_name = "admin_app/admin_login.html"

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None and user.is_staff:
            login(request, user)
            return redirect('admin_app:dashboard')
        else:
            context = {'error_message': 'Invalid username or password'}
            return render(request, self.template_name, context)
