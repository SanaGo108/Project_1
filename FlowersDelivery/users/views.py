from django.shortcuts import render, redirect
from .forms import RegistrationForm
from django.contrib.auth.views import LoginView
from .forms import ProfileForm

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = RegistrationForm()
    return render(request, 'users/register.html', {'form': form})

class UserLoginView(LoginView):
    template_name = 'users/login.html'

def edit_profile(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('account')
    else:
        form = ProfileForm(instance=request.user)
    return render(request, 'users/edit_profile.html', {'form': form})
