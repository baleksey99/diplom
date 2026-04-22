from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'diary'

urlpatterns = [
    path('', views.entry_list, name='entry_list'),
    path('search/', views.search_entries, name='search_entries'),
    path('create/', views.create_entry, name='create_entry'),
    path('<int:pk>/', views.view_entry, name='view_entry'),
    path('<int:pk>/edit/', views.edit_entry, name='edit_entry'),
    path('<int:pk>/delete/', views.delete_entry, name='delete_entry'),
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('register/', views.register, name='register'),
]