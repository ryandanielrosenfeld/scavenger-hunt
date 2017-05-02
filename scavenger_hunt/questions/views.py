from django.shortcuts import render
from .forms import InputForm, Task2ChoiceForm, Task9ChoiceForm
from django.http import HttpResponseRedirect
from .models import Task
from .services import activate_song
from .selenium_board_control import activate_board
from threading import Timer


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
            if request.POST['answer'].lower().strip() == 'lewin':
                correct = True
                activated = True
                request.user.task_num = 2
                request.user.save()
            else:
                incorrect = True
            return render(request, 'task1.html', {'form': form, 'correct': correct, 'incorrect': incorrect,
                                                  'activated': activated})
    return render(request, 'task1.html', {'form': form, 'activated': activated, 'hide_button': t_activated[0]})


def task1_activate(request):
    if request.user.task_num > 1:
        request.user.activate1 = True
        request.user.save()
        print("Activating T1")

        t_activated[0] = True
        timer = Timer(30.0, delay_show_btn_0)
        timer.start()
    return HttpResponseRedirect('/task1/')


def task2(request):
    form = Task2ChoiceForm()
    incorrect = False
    correct = False
    activated = False
    if request.user.task_num > 2:
        activated = True
    elif request.user.task_num < 2:
        url = "/task" + str(request.user.task_num) + "/"
        return HttpResponseRedirect(url)
    if request.method == 'POST':
        form = Task2ChoiceForm(request.POST)
        if form.is_valid():
            if request.POST['answer'] == 'JE':
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
        form = InputForm(request.POST)
        if form.is_valid():
            ans = request.POST['answer'].lower().strip()
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
            ans = request.POST['answer'].lower().strip()
            if ans == 'apple' or ans == 'mac':
                correct = True
                activated = True
                request.user.task_num = 5
                request.user.save()
            else:
                incorrect = True
            return render(request, 'task4.html', {'form': form, 'correct': correct, 'incorrect': incorrect,
                                                  'activated': activated})
    print(t_activated[1])
    return render(request, 'task4.html', {'form': form, 'activated': activated, 'hide_button': t_activated[1]})


def task4_activate(request):
    if request.user.task_num > 4:
        t = Task.objects.get(number=2)
        t.activated = True
        t.save()
        user = request.user
        name = user.first_name
        activate_board(name)

        t_activated[1] = True
        timer = Timer(30.0, delay_show_btn_1)
        timer.start()
        print(t_activated[1])
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
            ans = request.POST['answer'].lower().strip()
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
        form = InputForm(request.POST)
        if form.is_valid():
            ans = request.POST['answer'].lower().strip()
            if ans == 'national instruments' or ans == 'ni':
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
        form = InputForm(request.POST)
        if form.is_valid():
            ans = request.POST['answer'].lower().strip()
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
        form = InputForm(request.POST)
        if form.is_valid():
            ans = request.POST['answer'].lower().strip()
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
    form = Task9ChoiceForm()
    incorrect = False
    correct = False
    activated = False
    if request.user.task_num > 9:
        activated = True
    elif request.user.task_num < 9:
        url = "/task" + str(request.user.task_num) + "/"
        return HttpResponseRedirect(url)
    if request.method == 'POST':
        form = Task9ChoiceForm(request.POST)
        if form.is_valid():
            ans = request.POST['answer']
            if ans == 'C':
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
            ans = request.POST['answer'].lower().strip()
            if ans == '7.5':
                correct = True
                activated = True
                request.user.task_num = 11
                request.user.save()
            else:
                incorrect = True
            return render(request, 'task10.html', {'form': form, 'correct': correct, 'incorrect': incorrect,
                                                  'activated': activated})
    return render(request, 'task10.html', {'form': form, 'activated': activated, 'hide_button': t_activated[2]})


def task10_activate(request):
    if request.user.task_num > 10:
        activate_song()

        t_activated[2] = True
        t = Timer(120.0, delay_show_btn_2)
        t.start()
    return HttpResponseRedirect('/task10/')


t_activated = [False, False, False]


def delay_show_btn_0():
    t_activated[0] = False


def delay_show_btn_1():
    t_activated[1] = False


def delay_show_btn_2():
    t_activated[2] = False
