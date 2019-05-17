from django.contrib import admin
from .models import Role, Profile, TrustLevel
# Register your models here.


admin.site.register(Role)
admin.site.register(Profile)
admin.site.register(TrustLevel)
