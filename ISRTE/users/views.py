from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout, login, authenticate
from django.views.generic import View

from .models import Profile
from persons.models import Criminals
from access.models import GroupAccess, PersonAccess
# Create your views here.



def login_view(request):
    if request.POST:
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect("/")
            else:
                login_error = "Вам закрыто вход в систему"
                return render(request, "registration/login.html", {"login_error": login_error})
        else:
            login_error = 'Введено неправильные данные'
            return render(request, "registration/login.html", {"login_error": login_error})
    else:
        return render(request, "registration/login.html")


def logout_view(request):
    logout(request)
    return redirect('/accounts/login/')


@login_required
def users_list(request):
    users_list = Profile.objects.all().order_by('role_id')
    context = {
        "title": "Пользователи системы",
        "users": users_list
    }
    return render(request, "profiles/users_list.html", context)


@login_required
def user_profile(request, pk):
    profile = Profile.objects.get(id=pk)
    user_docs = Criminals.objects.filter(owner=profile)
    p_acc = PersonAccess.objects.filter(user_id=profile)
    context = {
        'profile': profile,
        'user_docs': user_docs,
        'p_acc': p_acc
    }
    return render(request, 'profiles/user_profile.html', context=context)



