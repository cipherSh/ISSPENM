from django.shortcuts import render, get_object_or_404, HttpResponse, redirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.views.generic import View
from django.db.models import Q

# models
from .models import Criminals, Persons, CriminalAddresses, Contacts, CriminalsRelatives, CriminalsContactPersons
from access.models import PersonAccess, GroupAccess
from law.models import Conviction, CriminalCaseCriminals, CriminalCase, Manhunt, Confluence

# forms
from .forms import CriminalCreateForm, PersonsCreateForm, CriminalAddRelativeForm, CriminalAddContactPersonForm, \
    CriminalAddAddressForm, CriminalContactDetailAddForm, CriminalOwnerChangeForm, CriminalConfidentChangeForm


# Create your views here.
@login_required
def record(request):
    return render(request, "persons/index.html")


@login_required
def criminals_page(request):
    criminals = Criminals.objects.order_by('-created')[:10]
    my_docs = Criminals.objects.filter(owner=request.user.profile).order_by('-created')[:10]
    uncheck_docs = Criminals.objects.filter(check=False).order_by('-created')[:10]
    context = {
        'criminals': criminals,
        'my_docs': my_docs,
        'uncheck_docs': uncheck_docs
    }
    return render(request, "persons/criminals_page.html", context=context)


@login_required
def criminal_my_docs(request):
    my_docs = Criminals.objects.filter(owner=request.user.profile).order_by('-created')
    context = {
        'my_docs': my_docs
    }
    return render(request, "persons/criminals_page.html", context=context)


@login_required
def criminal_uncheck_docs(request):
    uncheck_docs = Criminals.objects.filter(check=False).order_by('-created')[:10]
    context = {
        'uncheck_docs': uncheck_docs
    }
    return render(request, "persons/criminals_page.html", context=context)


@login_required
def criminals_list(request):
    search_query = request.GET.get('search_criminal', '')

    if search_query:
        criminals = Criminals.objects.filter(Q(full_name__icontains=search_query) | Q(INN__icontains=search_query))
    else:
        criminals = Criminals.objects.all()
    my_docs = Criminals.objects.filter(owner=request.user.profile)
    context = {
        'criminals': criminals,
        'my_docs': my_docs
    }
    return render(request, "persons/criminals_list.html", context=context)


@login_required
def criminal_close_change(request, pk):
    criminal = Criminals.objects.get(id=pk)
    if criminal.close == False:
        criminal.close = True
    else:
        criminal.close = False
    criminal.save()
    return redirect(criminal)


@login_required
def criminal_check(request, pk):
    criminal = Criminals.objects.get(id=pk)
    criminal.check = True
    criminal.save()
    return redirect(criminal)


@login_required
def criminal_single(request, pk):
    criminal = get_object_or_404(Criminals, id=pk)
    address = CriminalAddresses.objects.filter(criminal_id=criminal)
    contacts_detail = Contacts.objects.filter(criminal_id=criminal)
    relatives = CriminalsRelatives.objects.filter(criminal_id=criminal)
    contact_persons = CriminalsContactPersons.objects.filter(criminal_id=criminal)
    conviction = Conviction.objects.filter(criminal_id=criminal)
    manhunt = Manhunt.objects.filter(criminal_id=criminal)
    criminal_case = CriminalCaseCriminals.objects.filter(criminal_id=criminal)

    context = {
        "criminal": criminal,
        'address': address,
        'contacts_detail': contacts_detail,
        'relatives': relatives,
        'contact_persons': contact_persons,
        'convictions': conviction,
        'manhunt': manhunt,
        'criminal_case': criminal_case
    }
    if not request.user.is_superuser:

        if criminal.owner == request.user.profile:
            return render(request, "persons/criminal_single.html", context=context)

        elif criminal.close == True:
            return render(request, "persons/sorry.html")

        elif PersonAccess.objects.filter(doc_id=pk).filter(user_id=request.user.id):
            return render(request, "persons/criminal_single.html", context=context)

        else:
            gr = request.user.groups.all()
            ans = False
            for g in gr:
                if GroupAccess.objects.filter(doc_id=pk).filter(group_id=g.id):
                    ans = True
            if ans:
                return render(request, "persons/criminal_single.html", context=context)
            return render(request, "persons/sorry.html", {"gr": gr})
    return render(request, "persons/criminal_single.html", context=context)


@login_required
def citizen_list(request):
    persons = Persons.objects.all()
    return render(request, "persons/citizen_list.html", {"citizens": persons})


@login_required
def citizen_single(request, pk):
    citizen = get_object_or_404(Persons, id=pk)
    return render(request, "persons/citizen_single.html", {"criminal": citizen})


@login_required
def record_main_page(request):
    return render(request, "persons/home.html")


def search_form(request):
    return render(request, 'persons/search.html')

def search(request):
    if 'text' in request.GET and request.GET['text']:
        q = request.GET['text']
        criminals = Criminals.objects.filter(last_name__icontains=q)
        return render(request, 'persons/search_results.html', {'Criminals': criminals, 'query': q})
    else:
        return HttpResponse('Please submit a search term.')


class CriminalCreate(View):
    def get(self, request):
        form = CriminalCreateForm()
        return render(request, 'persons/criminal_create.html', context={'form': form})

    def post(self, request):
        bound_form = CriminalCreateForm(request.POST)

        if bound_form.is_valid():
            new_criminal = bound_form.save(commit=False)
            new_criminal.user = request.user.profile
            new_criminal.owner = request.user.profile
            new_criminal.full_name = new_criminal.last_name + ' ' + new_criminal.first_name + ' ' + \
                                     new_criminal.patronymic
            new_criminal.save()
            return redirect(new_criminal)
        return render(request, 'persons/criminal_create.html', context={'form': bound_form})


class CriminalUpdate(View):
    def get(self, request, pk):
        criminal = Criminals.objects.get(id=pk)
        bound_form = CriminalCreateForm(instance=criminal)
        return render(request, 'persons/criminal_update.html', context={'form': bound_form, 'criminal': criminal})

    def post(self, request, pk):
        criminal = Criminals.objects.get(id=pk)
        bound_form = CriminalCreateForm(request.POST, instance=criminal)
        if bound_form.is_valid():
            new_criminal = bound_form.save()
            return redirect(new_criminal)
        return render(request, 'persons/criminal_update.html', context={'form': bound_form, 'criminal': criminal})


class CriminalDelete(View):
    def get(self, request, pk):
        criminal = Criminals.objects.get(id=pk)
        return render(request, 'persons/criminal_delete.html', context={'criminal': criminal})

    def post(self, request, pk):
        criminal = Criminals.objects.get(id=pk)
        criminal.delete()
        return redirect(reverse('list_criminals'))


class CriminalContactDetailAddView(View):
    def get(self, request, pk):
        form = CriminalContactDetailAddForm()
        criminal = Criminals.objects.get(id=pk)
        return render(request, 'persons/add/criminal_contact_add.html', context={'form': form, 'criminal': criminal})

    def post(self, request, pk):
        bound_form = CriminalContactDetailAddForm(request.POST)
        criminal = Criminals.objects.get(id=pk)

        if bound_form.is_valid():
            new_contact = bound_form.save(commit=False)
            new_contact.criminal_id = criminal
            new_contact.save()
            return redirect(criminal)
        return render(request, 'persons/add/criminal_contact_add.html',
                      context={'form': bound_form, 'criminal': criminal})


class CriminalAddressAdd(View):
    def get(self, request, pk):
        form = CriminalAddAddressForm()
        criminal = Criminals.objects.get(id=pk)
        return render(request, 'persons/add/criminal_add_address.html', context={'form': form, 'criminal': criminal})

    def post(self, request, pk):
        bound_form = CriminalAddAddressForm(request.POST)
        criminal = Criminals.objects.get(id=pk)

        if bound_form.is_valid():
            new_address = bound_form.save(commit=False)
            new_address.criminal_id = criminal
            new_address.save()
            return redirect(criminal)
        return render(request, 'persons/add/criminal_add_address.html', context={'form': bound_form,
                                                                                 'criminal': criminal})


class CriminalAddRelative(View):
    def get(self, request, pk):
        criminal = Criminals.objects.get(id=pk)
        person_form = PersonsCreateForm()
        add_form = CriminalAddRelativeForm()
        return render(request, 'persons/add/criminal_add_relative.html', context={'person_form': person_form,
                                                                                  'add_form': add_form,
                                                                                  'criminal': criminal})

    def post(self, request, pk):
        bound_add_form = CriminalAddRelativeForm(request.POST)
        bound_person_form = PersonsCreateForm(request.POST)
        criminal = Criminals.objects.get(id=pk)

        if bound_add_form.is_valid() and bound_person_form.is_valid():
            new_person = bound_person_form.save(commit=False)
            new_person.user = request.user.profile
            new_person.save()
            new_add = bound_add_form.save(commit=False)
            new_add.criminal_id = criminal
            new_add.person_id = new_person
            new_add.save()
            return redirect(criminal)
        return render(request, 'persons/add/criminal_add_relative.html', context={'person_form': bound_person_form,
                                                                                  'add_form': bound_add_form,
                                                                                  'criminal': criminal})


class CriminalAddContactPersonView(View):
    def get(self, request, pk):
        criminal = Criminals.objects.get(id=pk)
        person_form = PersonsCreateForm()
        add_form = CriminalAddContactPersonForm()
        return render(request, 'persons/add/criminal_add_contact-person.html', context={'person_form': person_form,
                                                                                        'add_form': add_form,
                                                                                        'criminal': criminal})

    def post(self, request, pk):
        bound_add_form = CriminalAddContactPersonForm(request.POST)
        bound_person_form = PersonsCreateForm(request.POST)
        criminal = Criminals.objects.get(id=pk)

        if bound_add_form.is_valid() and bound_person_form.is_valid():
            new_person = bound_person_form.save(commit=False)
            new_person.user = request.user.profile
            new_person.save()
            new_add = bound_add_form.save(commit=False)
            new_add.criminal_id = criminal
            new_add.person_id = new_person
            new_add.save()
            return redirect(criminal)
        return render(request, 'persons/add/criminal_add_contact-person.html',
                      context={'person_form': bound_person_form,
                               'add_form': bound_add_form,
                               'criminal': criminal})


class CriminalOwnerChangeView(View):
    def get(self, request, pk):
        criminal = Criminals.objects.get(id=pk)
        bound_form = CriminalOwnerChangeForm(instance=criminal)
        return render(request, 'persons/add/criminal_owner_change.html', context={'form': bound_form,
                                                                                  'criminal': criminal})

    def post(self, request, pk):
        criminal = Criminals.objects.get(id=pk)
        bound_form = CriminalOwnerChangeForm(request.POST, instance=criminal)
        if bound_form.is_valid():
            bound_form.save()
            return redirect(criminal)
        return render(request, 'persons/add/criminal_owner_change.html', context={'form': bound_form,
                                                                                  'criminal': criminal})


class CriminalConfidentChangeView(View):
    def get(self, request, pk):
        criminal = Criminals.objects.get(id=pk)
        bound_form = CriminalConfidentChangeForm(instance=criminal)
        return render(request, 'persons/add/criminal_confident_change.html', context={'form': bound_form,
                                                                                      'criminal': criminal})

    def post(self, request, pk):
        criminal = Criminals.objects.get(id=pk)
        bound_form = CriminalConfidentChangeForm(request.POST, instance=criminal)
        if bound_form.is_valid():
            bound_form.save()
            return redirect(criminal)
        return render(request, 'persons/add/criminal_confident_change.html', context={'form': bound_form,
                                                                                      'criminal': criminal})