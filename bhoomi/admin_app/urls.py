from django.urls import path
from .views import home as admin_home, signup, signin, profile, update_profile, delete_profile

app_name = 'admin_app'

urlpatterns = [
    path('', signup, name='signup'),  # Admin home/dashboard
    path('signin/', signin, name='login'),
    path('admin_home/', admin_home, name='admin_home'),
    path('profile/', profile, name='profile'),
    path('profile/update/', update_profile, name='update_profile'),
    path('profile/delete/', delete_profile, name='delete_profile'),
]
