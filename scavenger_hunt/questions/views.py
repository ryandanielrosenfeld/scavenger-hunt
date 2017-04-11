from django.shortcuts import render
from .forms import *


def task1(request):
    correct = False
    incorrect = False
    if request.method == 'POST':
        form = Task1Form(request.POST)
        if form.is_valid():
            if request.POST['answer'] == '1924':
                correct = True
                request.user.activate = True
            else:
                incorrect = True
            return render(request, 'task1.html', {'form': form, 'correct': correct, 'incorrect': incorrect})
    form = Task1Form()
    request.user.task_num = 1
    return render(request, 'task1.html', {'form': form})
