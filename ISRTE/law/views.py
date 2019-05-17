from django.shortcuts import render, redirect
from django.views.generic import View

#models
from .models import Conviction
from persons.models import Criminals

#forms
from .forms import CriminalConvictionAddForm, CriminalCaseCreateForm, CriminalsCriminalCaseAddForm, \
    CriminalManhuntAddForm


# Create your views here.


class CriminalConvictionAddView(View):
    def get(self, request, pk):
        form = CriminalConvictionAddForm()
        criminal = Criminals.objects.get(id=pk)
        context = {
            'criminal': criminal,
            'form': form,
        }
        return render(request, 'law/conviction_add.html', context=context)

    def post(self, request, pk):
        bound_form = CriminalConvictionAddForm(request.POST)
        criminal = Criminals.objects.get(id=pk)
        context = {
            'criminal': criminal,
            'form': bound_form,
        }

        if bound_form.is_valid():
            new_conviction = bound_form.save(commit=False)
            new_conviction.criminal_id = criminal
            new_conviction.save()
            return redirect(criminal)
        return render(request, 'law/conviction_add.html', context=context)


class CriminalCriminalCaseAddView(View):
    def get(self, request, pk):
        criminal = Criminals.objects.get(id=pk)
        case_form = CriminalCaseCreateForm()
        case_add_form = CriminalsCriminalCaseAddForm()
        context = {
            'criminal': criminal,
            'case_form': case_form,
            'case_add_form': case_add_form
        }
        return render(request, 'law/criminal_case_add.html', context=context)

    def post(self, request, pk):
        criminal = Criminals.objects.get(id=pk)
        bound_case_form = CriminalCaseCreateForm(request.POST)
        bound_case_add_form = CriminalsCriminalCaseAddForm(request.POST)
        context = {
            'criminal': criminal,
            'case_form': bound_case_form,
            'case_add_form': bound_case_add_form
        }

        if bound_case_form.is_valid() and bound_case_add_form.is_valid():
            new_case = bound_case_form.save()
            new_add_case = bound_case_add_form.save(commit=False)
            new_add_case.criminal_id = criminal
            new_add_case.criminal_case = new_case
            new_add_case.save()
            return redirect(criminal)
        return render(request, 'law/criminal_case_add.html', context=context)


class CriminalManhuntAddView(View):
    def get(self, request, pk):
        criminal = Criminals.objects.get(id=pk)
        form = CriminalManhuntAddForm()

        context = {
            'criminal': criminal,
            'form': form,
        }
        return render(request, 'law/manhunt_add.html', context=context)

    def post(self, request, pk):
        criminal = Criminals.objects.get(id=pk)
        bound_form = CriminalManhuntAddForm(request.POST)
        context = {
            'criminal': criminal,
            'form': bound_form,
        }
        if bound_form.is_valid():
            new_manhunt = bound_form.save(commit=False)
            new_manhunt.criminal_id = criminal
            new_manhunt.save()
            return redirect(criminal)
        return render(request, 'law/manhunt_add.html', context=context)