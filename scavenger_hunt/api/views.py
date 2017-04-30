from django.shortcuts import render
from general.models import SiteUser


def api_call(request):
    response = 'n'
    if request.method == 'GET':
        tn = request.GET.get('task_num', None)
        if tn == '1':
            activated_users = SiteUser.objects.filter(activate1=True)
            if len(activated_users) > 0:
                response = 'y'
                for user in activated_users:
                    user.activate1 = False
                    user.save()
        elif tn == '2':
            activated_users = SiteUser.objects.filter(activate2=True)
            if len(activated_users) > 0:
                response = 'y'
                for user in activated_users:
                    user.activate2 = False
                    user.save()
    return render(request, 'response.html', {'response': response})
