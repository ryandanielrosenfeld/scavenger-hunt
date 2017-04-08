from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login
from .forms import RegisterForm, LoginForm
from .models import SiteUser


def register(request):
    if request.method == 'POST':
        reg_form = RegisterForm(request.POST)
        login_form = LoginForm(request.POST)
        if reg_form.is_valid():
            user = SiteUser.objects.create_user(request.POST['email'], request.POST['email'], request.POST['password'])
            user.first_name = request.POST['first_name']
            user.last_name = request.POST['last_name']
            user.save()
            login(request, user)
            return render(request, 'questions/index.html')
        elif login_form.is_valid():
            user = authenticate(username=request.POST['username'], password=request.POST['password'])
            if user is not None:
                login(user)
                return HttpResponseRedirect('/')
    reg_form = RegisterForm()
    login_form = LoginForm()
    return render(request, 'general/register.html', {'login_form': login_form, 'reg_form': reg_form})


def index(request):
    if request.user.is_authenticated():
        return render(request, 'index.html')
    return HttpResponseRedirect('/register/')
