from django.shortcuts import render
import json
from general.models import SiteUser


def api_call(request):
    response = json.dumps({'None': True})
    if request.method == 'GET':
        task_num = request.GET.get('task_num', None)
        if task_num == '1':
            activate = SiteUser.objects.filter(task_num=1, activate=True)
            if len(activate) > 0:
                response = 1
                for user in activate:
                    user.activate = False
                    user.task_num += 1
                    user.save()
            else:
                response = 0
    return render(request, 'response.html', {'response': response})
