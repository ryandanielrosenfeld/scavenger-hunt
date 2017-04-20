from django.conf.urls import url
from django.contrib import admin
from general import views as general_views
from questions import views as question_views
from api import views as api_views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^register/', general_views.register),
    url(r'^$', general_views.index),
    url(r'^task1/', question_views.task1),
    url(r'^task1/activate/', question_views.task1_activate),
    url(r'^task2/', question_views.task2),
    url(r'^api/', api_views.api_call)
]
