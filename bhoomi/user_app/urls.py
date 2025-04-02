from django.urls import path, include
from .views import (home,signup, profile, update_profile, delete_profile, 
                    bin_manager, risk_alerts, eco_cleanup )  # Import the signup view

urlpatterns = [
    # ... other URL patterns ...
    path('', home, name='home'),  # Home page
    path('accounts/', include('django.contrib.auth.urls')),
    path('signup/', signup, name='signup'),
    path('profile/', profile, name='profile'),
    path('profile/update/', update_profile, name='update_profile'),
    path('profile/delete/', delete_profile, name='delete_profile'),
     path('bin-manager/', bin_manager, name='bin_manager'),  # Add this
    path('risk-alerts/', risk_alerts, name='risk_alerts'),  # Add this
    path('eco-cleanup/', eco_cleanup, name='eco_cleanup'),
]
