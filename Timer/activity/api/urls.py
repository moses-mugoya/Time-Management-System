from django.urls import re_path
from . import views


urlpatterns = [
    re_path('^$', views.ActivityListView.as_view(), name='list'),
    re_path(r'^create/', views.ActivityCreateView.as_view(), name='create'),
    re_path(r'^(?P<pk>\d+)/$', views.ActivityDetailView.as_view(), name='detail'),
    re_path(r'^(?P<pk>\d+)/update/$', views.ActivityUpdateApiView.as_view(), name='update'),
    re_path(r'^(?P<pk>\d+)/delete/$', views.ActivityDestroyApiView.as_view(), name='delete'),
    # re_path('^add/activity/$', views.add_activity, name='add'),
    # re_path(r'^edit/(?P<id>\d+)/$', views.edit_activity, name='edit'),
    # re_path(r'^delete/(?P<id>\d+)/$', views.delete_activity, name='delete'),
]