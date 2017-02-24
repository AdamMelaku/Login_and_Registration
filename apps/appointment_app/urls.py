from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^register_user$', views.register_user),
    url(r'^login_user$', views.login_user),
    url(r'^logout$', views.logout),
    url(r'^appointments$', views.dashboard),
    url(r'^appointments/(?P<id>\d+)$', views.update_appoitment),
    url(r'^delete/(?P<id>\d+)$', views.delete)
]
