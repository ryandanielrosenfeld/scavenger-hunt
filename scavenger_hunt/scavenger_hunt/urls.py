from django.conf.urls import url
from django.contrib import admin
from general import views as general_views
from questions import views as question_views
from api import views as api_views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^register/', general_views.register),
    url(r'^$', general_views.index),
    url(r'^task1/activate/', question_views.task1_activate),
    url(r'^task1/', question_views.task1),
    url(r'^task2/', question_views.task2),
    url(r'^task3/', question_views.task3),
    url(r'^task4/activate/', question_views.task4_activate),
    url(r'^task4/', question_views.task4),
    url(r'^task5/', question_views.task5),
    url(r'^task6/', question_views.task6),
    url(r'^task7/', question_views.task7),
    url(r'^task8/', question_views.task8),
    url(r'^task9/', question_views.task9),
    url(r'^task10/activate/', question_views.task10_activate),
    url(r'^task10/', question_views.task10),
    url(r'^api/', api_views.api_call),
    url(r'^logout/', general_views.logout_view, name='logout'),
    url(r'^test/', general_views.test_view),
]
