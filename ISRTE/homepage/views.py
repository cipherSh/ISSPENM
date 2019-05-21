from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from persons.models import Criminals, Persons
from law.models import Manhunt, CriminalCase
from users.models import Profile
from django.contrib.auth.models import User

# Create your views here.


@login_required(login_url='/accounts/login/')
def homepage(request):
    criminal = Criminals.objects.all().count()
    terr = Criminals.objects.filter(occupation=1).count()
    persons = Persons.objects.all().count()
    cp = criminal+persons
    manhunt = Manhunt.objects.all().count()
    case = CriminalCase.objects.all().count()
    mc = manhunt+case
    profile = Profile.objects.all().count()
    active = User.objects.filter(is_active=True).count()
    deactive = profile-active
    context = {
        'criminal': criminal,
        'persons': persons,
        'cp': cp,
        'terr': terr,
        'manhunt': manhunt,
        'case': case,
        'profile': profile,
        'active': active,
        'deactive': deactive,
        'mc': mc
    }
    return render(request, "homepage/homepage.html", context=context)