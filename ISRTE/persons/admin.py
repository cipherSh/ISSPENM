from django.contrib import admin
from .models import Criminals, Persons, CriminalAddresses, ContactRelation, ContactType, Contacts, \
    PersonAddresses, Occupation, RelativeRelation, Organizations, CriminalsRelatives, CriminalsContactPersons


# Register your models here.

@admin.register(Criminals)
class CriminalsAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'patronymic', 'INN')
    list_filter = ('status', 'marital_status')


admin.site.register(Occupation)
admin.site.register(Organizations)
admin.site.register(Persons)
admin.site.register(CriminalAddresses)
admin.site.register(Contacts)
admin.site.register(ContactType)
admin.site.register(ContactRelation)
admin.site.register(RelativeRelation)
admin.site.register(PersonAddresses)
admin.site.register(CriminalsRelatives)
admin.site.register(CriminalsContactPersons)
