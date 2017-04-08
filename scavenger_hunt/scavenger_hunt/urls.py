from django.conf.urls import url
from django.contrib import admin
from general import views as general_views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', general_views.index),
]
