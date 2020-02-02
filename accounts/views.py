from django.shortcuts import render, redirect
from accounts.forms import RegistrationForm
from django.contrib.auth.models import User

# Create your views here.


def home(request):
    numbers = [1, 2, 3, 4, 5]
    name = 'sravan_kumar'

    args = {
        'name': name,
        'numbers': numbers
    }
    return render(request, 'accounts/home.html', args)


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/accounts')
    else:
        form = RegistrationForm()
        args = {'form': form}
        return render(request, 'accounts/register.html', args)


def profile(request):
    args = {'user': request.user}
    return render(request, 'accounts/profile.html')
