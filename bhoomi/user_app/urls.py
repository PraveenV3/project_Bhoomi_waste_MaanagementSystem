from django.urls import path, include
from .views import home,signup, profile, update_profile, delete_profile  # Import the signup view

urlpatterns = [
    # ... other URL patterns ...
    path('', home, name='home'),  # Home page
    path('accounts/', include('django.contrib.auth.urls')),
    path('signup/', signup, name='signup'),
    path('profile/', profile, name='profile'),
    path('profile/update/', update_profile, name='update_profile'),
    path('profile/delete/', delete_profile, name='delete_profile'),
]
