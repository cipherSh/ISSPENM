from django import forms
from .models import Criminals, Persons, CriminalsRelatives, CriminalsContactPersons, CriminalAddresses, Contacts


class CriminalCreateForm(forms.ModelForm):
    class Meta:
        model = Criminals
        fields = ['first_name', 'last_name', 'patronymic', 'birthday', 'birth_country', 'birth_region',
                  'birth_District', 'birth_City', 'birth_Village', 'gender', 'citizenship', 'INN', 'passport_serial',
                  'passport_number', 'issue_organ', 'issue_data', 'education', 'education_place', 'profession',
                  'marital_status', 'occupation', 'status', 'image', 'organization', 'remarks', 'close', 'confident']


class PersonsCreateForm(forms.ModelForm):
    class Meta:
        model = Persons
        fields = ['first_name', 'last_name', 'patronymic', 'birthday', 'birth_country', 'birth_region',
                  'birth_District', 'birth_City', 'birth_Village', 'gender', 'citizenship', 'INN', 'passport_serial',
                  'passport_number', 'issue_organ', 'issue_data', 'education', 'education_place', 'profession',
                  'job', 'workplace', 'marital_status', 'phone', 'email', 'status', 'image', 'remarks']


class CriminalAddRelativeForm(forms.ModelForm):
    class Meta:
        model = CriminalsRelatives
        fields = ['relation']


class CriminalAddContactPersonForm(forms.ModelForm):
    class Meta:
        model = CriminalsContactPersons
        fields = ['relation']


class CriminalAddAddressForm(forms.ModelForm):
    class Meta:
        model = CriminalAddresses
        fields = ['kind', 'region', 'district', 'city', 'village', 'micro_district', 'street', 'home', 'date_entry',
                  'date_release', 'remarks']


class CriminalContactDetailAddForm(forms.ModelForm):
    class Meta:
        model = Contacts
        fields = ['type_contact', 'contact', 'remarks']

