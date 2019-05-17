from django.shortcuts import render, redirect, HttpResponse
from django.views.generic import View
from .forms import GroupAccessForm, PersonalAccessForm
from persons.models import Criminals

# Create your views here.


class GroupAccessCreate(View):
    def get(self, request, pk):
        criminal = Criminals.objects.get(id=pk)
        form = GroupAccessForm()
        return render(request, 'access/group_access_create.html', context={'form': form, 'criminal': criminal})

    def post(self, request, pk):
        bound_form = GroupAccessForm(request.POST)
        criminal = Criminals.objects.get(id=pk)

        if bound_form.is_valid():
            new_access = bound_form.save(commit=False)
            new_access.doc_id = criminal
            new_access.save()
            return redirect(criminal)
        return render(request, 'access/group_access_create.html', context={'form': bound_form, 'criminal': criminal})


class PersonalAccessCreate(View):
    def get(self, request, pk):
        criminal = Criminals.objects.get(id=pk)
        form = PersonalAccessForm()
        return render(request, 'access/personal_access_create.html', context={'form': form, 'criminal': criminal})

    def post(self, request, pk):
        bound_form = PersonalAccessForm(request.POST)
        criminal = Criminals.objects.get(id=pk)

        if bound_form.is_valid():
            new_access = bound_form.save(commit=False)
            new_access.doc_id = criminal
            new_access.save()
            return redirect(criminal)
        return render(request, 'access/personal_access_create.html', context={'form': bound_form, 'criminal': criminal})
