from django.urls import path, include
from .views import signup  # Import the signup view

urlpatterns = [
    # ... other URL patterns ...
    path('accounts/', include('django.contrib.auth.urls')),
    path('signup/', signup, name='signup'),
]
