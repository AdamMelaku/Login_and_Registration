from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^process$', views.process, name="process"),
    url(r'^login_user$', views.login_user, name="login_user"),
    url(r'^success$', views.success, name="success")
]
