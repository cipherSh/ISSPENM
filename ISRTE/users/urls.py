from django.views.generic.base import RedirectView
from django.urls import path
from . import views

urlpatterns = [
    path('', views.users_list, name='users_list'),
    path('create/', RedirectView.as_view(url='/admin/users/profile/add/', permanent=False),
         name='create_user_url'),
    path('profile/<int:pk>', views.user_profile, name='user_profile_url'),
    path('login/', views.login_view, name='Login'),
    path('logout/', views.logout_view, name='Logout'),
]
