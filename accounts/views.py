from django.shortcuts import render, redirect
from . import models
from django.contrib import messages
from django.contrib.auth import login, authenticate, update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from . import forms


def signup(request):
    if request.method == 'POST':
        user_form = forms.SignUpForm(request.POST)
        profile_form = forms.ProfileForm(request.POST, request.FILES)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            username = user_form.cleaned_data['username']
            raw_psw = user_form.cleaned_data['password1']
            user = authenticate(username=username, password=raw_psw)
            login(request, user)
            return redirect('home')
    else:
        user_form = forms.SignUpForm()
        profile_form = forms.ProfileForm()
    return render(request, 'accounts/signup.html', {'user_form': user_form,
                                                    'profile_form': profile_form})


@login_required
def edit_user(request):
    profile = models.Profile.objects.get(user=request.user)
    if request.method == 'POST':
        user_form = forms.EditUserForm(request.POST, instance=request.user)
        profile_form = forms.ProfileForm(request.POST, request.FILES, instance=profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'your info has been updated')
        else:
            messages.error(request, 'there was an error, please try again')
    else:
        user_form = forms.EditUserForm(instance=request.user)
        profile_form = forms.ProfileForm(instance=profile)
    return render(request, 'accounts/edit_user.html', {'user_form': user_form,
                                                       'profile_form': profile_form})


@login_required
def dash_bord(request):
    profile = models.Profile.objects.get(user=request.user)
    return render(request, 'accounts/dashbord.html')
