from django.shortcuts import render
import json
from questions.models import Task


def api_call(request):
    response = 'n'
    if request.method == 'GET':
        tn = request.GET.get('task_num', None)
        task = Task.objects.get(number=tn)
        print(task.number, task.activated)
        if task.activated:
            response = 'y'
            task.activated = False
            task.save()
            print(task.number, task.activated, '|||||||')
    return render(request, 'response.html', {'response': response})
