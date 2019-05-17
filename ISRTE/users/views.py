from django.shortcuts import render, redirect
from .forms import UserForm, ProfileForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.contrib.auth import logout, login, authenticate
from .models import Profile
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import View

# Create your views here.


@login_required
@transaction.atomic
def update_profile(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=request.user)
        profile_form = ProfileForm(request.POST, instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, ('Ваш профиль был успешно обновлен!',))
            return redirect('/users/')
        else:
            messages.error(request, ('Пожалуйста, исправьте ошибки.',))
    else:
        user_form = UserForm(instance=request.user)
        profile_form = ProfileForm(instance=request.user.profile)
    return render(request, 'profiles/profile.html', {
        'user_form': user_form,
        'profile_form': profile_form
    })


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
def profile_detail(request, user):
    profile = Profile.objects.get(user=user)
    return render(request, "profiles/profile_detail.html", context={'profile': profile})

@login_required
def create_user(request):
    args = {}
    args['form'] = UserCreationForm()
    if request.POST:
        newuser_form = UserCreationForm(request.POST)
        if newuser_form.is_valid():
            newuser_form.save()
            return render(request, "success-uc.html")
        else:
            args['form'] = newuser_form
    return render(request, "profiles/createuser.html", args)


class UserCreate(View):
    def get(self, request):
        form = UserForm()
        return render(request, 'profiles/usercreate.html', context={'form': form})

    def post(self, request):
        bound_form = UserForm(request.POST)
        if bound_form.is_valid():
            new_user = bound_form.save()
            return redirect(new_user)
        return render(request, 'profiles/usercreate.html', context={'form': bound_form})


class ProfileUpdate(View):
    def get(self, request, user):
        profile = Profile.objects.get(user=user)
        bound_form = ProfileForm(instance=profile)
        return render(request, 'profiles/profile_update.html', context={'form': bound_form, 'profile': profile})