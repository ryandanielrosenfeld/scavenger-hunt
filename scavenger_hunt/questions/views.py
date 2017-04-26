from django.shortcuts import render
from .forms import *
from django.http import HttpResponseRedirect
from .models import Task
from .services import activate_song
from .selenium_board_control import activate_board


def task1(request):
    form = InputForm()
    incorrect = False
    correct = False
    activated = False
    if request.user.task_num > 1:
        activated = True
    else:
        request.user.task_num = 1
        request.user.save()
    if request.method == 'POST':
        form = InputForm(request.POST)
        if form.is_valid():
            if request.POST['answer'] == 'Lewin':
                correct = True
                activated = True
                request.user.task_num = 2
                request.user.save()
            else:
                incorrect = True
            return render(request, 'task1.html', {'form': form, 'correct': correct, 'incorrect': incorrect,
                                                  'activated': activated})
    return render(request, 'task1.html', {'form': form, 'activated': activated})


def task1_activate(request):
    t = Task.objects.get(number=1)
    t.activate = True
    t.save()
    return HttpResponseRedirect('/task1/')


def task2(request):
    form = InputForm()
    incorrect = False
    correct = False
    activated = False
    if request.user.task_num > 2:
        activated = True
    elif request.user.task_num < 2:
        url = "/task" + str(request.user.task_num) + "/"
        return HttpResponseRedirect(url)
    if request.method == 'POST':
        form = InputForm(request.POST)  # MAKE MULTIPLE CHOICE (hoverboard, electric guitar, rotunda)
        if form.is_valid():
            if request.POST['answer'] == 'A Jet Engine':
                correct = True
                activated = True
                request.user.task_num = 3
                request.user.save()
            else:
                incorrect = True
            return render(request, 'task2.html', {'form': form, 'correct': correct, 'incorrect': incorrect,
                                                  'activated': activated})
    return render(request, 'task2.html', {'form': form, 'activated': activated})


def task3(request):
    form = InputForm()
    incorrect = False
    correct = False
    activated = False
    if request.user.task_num > 3:
        activated = True
    elif request.user.task_num < 3:
        url = "/task" + str(request.user.task_num) + "/"
        return HttpResponseRedirect(url)
    if request.method == 'POST':
        form = InputForm(request.POST)  # MAKE MULTIPLE CHOICE (hoverboard, electric guitar, rotunda)
        if form.is_valid():
            ans = request.POST['answer'].lower()
            if ans == 'material science' or ans == 'material science building':
                correct = True
                activated = True
                request.user.task_num = 4
                request.user.save()
            else:
                incorrect = True
            return render(request, 'task3.html', {'form': form, 'correct': correct, 'incorrect': incorrect,
                                                  'activated': activated})
    return render(request, 'task3.html', {'form': form, 'activated': activated})


def task4(request):
    form = InputForm()
    incorrect = False
    correct = False
    activated = False
    if request.user.task_num > 4:
        activated = True
    elif request.user.task_num < 4:
        url = "/task" + str(request.user.task_num) + "/"
        return HttpResponseRedirect(url)
    if request.method == 'POST':
        form = InputForm(request.POST)
        if form.is_valid():
            if request.POST['answer'].lower() == 'apple':
                correct = True
                activated = True
                request.user.task_num = 5
                request.user.save()
            else:
                incorrect = True
            return render(request, 'task4.html', {'form': form, 'correct': correct, 'incorrect': incorrect,
                                                  'activated': activated})
    return render(request, 'task4.html', {'form': form, 'activated': activated})


def task4_activate(request):
    t = Task.objects.get(number=4)
    t.activate = True
    t.save()
    user = request.user
    name = user.first_name
    activate_board(name)
    return HttpResponseRedirect('/task4/')


def task5(request):
    form = InputForm()
    incorrect = False
    correct = False
    activated = False
    if request.user.task_num > 5:
        activated = True
    elif request.user.task_num < 5:
        url = "/task" + str(request.user.task_num) + "/"
        return HttpResponseRedirect(url)
    if request.method == 'POST':
        form = InputForm(request.POST)
        if form.is_valid():
            ans = request.POST['answer'].lower()
            print(ans)
            if ans == 'at&t':
                correct = True
                activated = True
                request.user.task_num = 6
                request.user.save()
            else:
                incorrect = True
            return render(request, 'task5.html', {'form': form, 'correct': correct, 'incorrect': incorrect,
                                                  'activated': activated})
    return render(request, 'task5.html', {'form': form, 'activated': activated})


def task6(request):
    form = InputForm()
    incorrect = False
    correct = False
    activated = False
    if request.user.task_num > 6:
        activated = True
    elif request.user.task_num < 6:
        url = "/task" + str(request.user.task_num) + "/"
        return HttpResponseRedirect(url)
    if request.method == 'POST':
        form = InputForm(request.POST)  # MAKE MULTIPLE CHOICE (hoverboard, electric guitar, rotunda)
        if form.is_valid():
            ans = request.POST['answer'].lower()
            if ans == 'national instruments':
                correct = True
                activated = True
                request.user.task_num = 7
                request.user.save()
            else:
                incorrect = True
            return render(request, 'task6.html', {'form': form, 'correct': correct, 'incorrect': incorrect,
                                                  'activated': activated})
    return render(request, 'task6.html', {'form': form, 'activated': activated})


def task7(request):
    form = InputForm()
    incorrect = False
    correct = False
    activated = False
    if request.user.task_num > 7:
        activated = True
    elif request.user.task_num < 7:
        url = "/task" + str(request.user.task_num) + "/"
        return HttpResponseRedirect(url)
    if request.method == 'POST':
        form = InputForm(request.POST)  # MAKE MULTIPLE CHOICE (hoverboard, electric guitar, rotunda)
        if form.is_valid():
            ans = request.POST['answer'].lower()
            if ans == 'zimbabwe':
                correct = True
                activated = True
                request.user.task_num = 8
                request.user.save()
            else:
                incorrect = True
            return render(request, 'task7.html', {'form': form, 'correct': correct, 'incorrect': incorrect,
                                                  'activated': activated})
    return render(request, 'task7.html', {'form': form, 'activated': activated})


# GET RID OF SPACES


def task8(request):
    form = InputForm()
    incorrect = False
    correct = False
    activated = False
    if request.user.task_num > 8:
        activated = True
    elif request.user.task_num < 8:
        url = "/task" + str(request.user.task_num) + "/"
        return HttpResponseRedirect(url)
    if request.method == 'POST':
        form = InputForm(request.POST)  # MAKE MULTIPLE CHOICE (hoverboard, electric guitar, rotunda)
        if form.is_valid():
            ans = request.POST['answer'].lower()
            if ans == '15':
                correct = True
                activated = True
                request.user.task_num = 9
                request.user.save()
            else:
                incorrect = True
            return render(request, 'task8.html', {'form': form, 'correct': correct, 'incorrect': incorrect,
                                                  'activated': activated})
    return render(request, 'task8.html', {'form': form, 'activated': activated})


def task9(request):
    form = InputForm()
    incorrect = False
    correct = False
    activated = False
    if request.user.task_num > 9:
        activated = True
    elif request.user.task_num < 9:
        url = "/task" + str(request.user.task_num) + "/"
        return HttpResponseRedirect(url)
    if request.method == 'POST':
        form = InputForm(request.POST)  # MAKE MULTIPLE CHOICE (hoverboard, electric guitar, rotunda)
        if form.is_valid():
            ans = request.POST['answer'].lower()
            if ans == 'concrete lightning':
                correct = True
                activated = True
                request.user.task_num = 10
                request.user.save()
            else:
                incorrect = True
            return render(request, 'task9.html', {'form': form, 'correct': correct, 'incorrect': incorrect,
                                                  'activated': activated})
    return render(request, 'task9.html', {'form': form, 'activated': activated})


def task10(request):
    form = InputForm()
    incorrect = False
    correct = False
    activated = False
    if request.user.task_num > 10:
        activated = True
    else:
        request.user.task_num = 10
        request.user.save()
    if request.method == 'POST':
        form = InputForm(request.POST)
        if form.is_valid():
            if request.POST['answer'] == '7.5':
                correct = True
                activated = True
                request.user.task_num = 11
                request.user.save()
            else:
                incorrect = True
            return render(request, 'task1.html', {'form': form, 'correct': correct, 'incorrect': incorrect,
                                                  'activated': activated})
    return render(request, 'task10.html', {'form': form, 'activated': activated})


def task10_activate(request):
    activate_song()
    return HttpResponseRedirect('/task10/')
