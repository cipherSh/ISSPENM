from django.contrib import admin
from .models import Conviction, CriminalCase, Confluence, Manhunt

# Register your models here.

admin.site.register(CriminalCase)
admin.site.register(Confluence)
admin.site.register(Conviction)
admin.site.register(Manhunt)

