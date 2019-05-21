
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('persons/', include('persons.urls')),
    path('users/', include('users.urls')),
    path('accounts/', include('users.urls')),
    path('access/', include('access.urls')),
    path('law/', include('law.urls')),
    path('', include('homepage.urls'))
]
