from django.urls import re_path
from . import views

app_name = 'activity'

urlpatterns = [
    re_path('^$', views.index, name='index'),
    re_path('^activities/$', views.activity_list, name='list'),
    re_path('^add/activity/$', views.add_activity, name='add'),
    re_path(r'^edit/(?P<id>\d+)/$', views.edit_activity, name='edit'),
    re_path(r'^delete/(?P<pk>\d+)/$', views.delete_activity, name='delete'),
]
