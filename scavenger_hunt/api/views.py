from django.shortcuts import render
import json
from questions.models import Task


def api_call(request):
    response = json.dumps({'None': True})
    if request.method == 'GET':
        tn = request.GET.get('task_num', None)
        task = Task.objects.get(number=tn)
        if task.activate:
            response = 1
            task.activate = False
            task.save()
        else:
            response = 0
    return render(request, 'response.html', {'response': response})
