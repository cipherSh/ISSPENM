from django import forms
from .models import Conviction, CriminalCase, CriminalCaseCriminals, Manhunt


class CriminalCaseCreateForm(forms.ModelForm):
    class Meta:
        model = CriminalCase
        fields = ['number', 'year', 'article', 'organ', 'date_arousal', 'date_suspension', 'remarks']


class CriminalsCriminalCaseAddForm(forms.ModelForm):
    class Meta:
        model = CriminalCaseCriminals
        fields = []


class CriminalManhuntAddForm(forms.ModelForm):
    class Meta:
        model = Manhunt
        fields = ['invest_case_number', 'criminalCase_id', 'date_arousal', 'invest_initiator', 'invest_category',
                  'circular_number', 'preventive', 'date_inter_invest', 'invest_stopped', 'place_detention',
                  'date_detention', 'invest_stopped_circular']


class CriminalConvictionAddForm(forms.ModelForm):
    class Meta:
        model = Conviction
        fields = ['criminal_case_number', 'criminal_case_year', 'criminal_case_organ', 'law_article', 'date_sentence',
                  'date_release']
