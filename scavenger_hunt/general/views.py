from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login


# Create your views here.
def index(request):
    return render(request, 'general/index.html')
