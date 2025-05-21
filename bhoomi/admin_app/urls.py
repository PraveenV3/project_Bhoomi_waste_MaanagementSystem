from django.urls import path
from . import views

app_name = 'admin_app'

urlpatterns = [
    path("", views.AdminLoginView.as_view(), name="admin_login"),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('logout/', views.admin_logout, name='logout'),
]
