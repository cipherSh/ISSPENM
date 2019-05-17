from django.urls import path
from . import views

urlpatterns = [
    path('', views.users_list, name='users_list'),
    path('profile/<int:user>', views.profile_detail, name='single_profile'),
    path('create/', views.create_user, name='Login'),
    path('profile/<str: user>/update', views.ProfileUpdate.as_view(), name='profile_update_url'),
    path('login/', views.login_view, name='Login'),
    path('logout/', views.logout_view, name='Logout'),
]
