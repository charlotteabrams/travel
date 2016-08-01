from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.index, name = 'my_login_index'),
    url(r'^register/$', views.register, name = 'my_login_register'),
    url(r'^login/$', views.processlogin, name = 'my_login_login'),
    url(r'^logout/$', views.logout, name = 'my_login_logout'),
    url(r'^process/$', views.processregister, name = 'my_login_process'),
    url(r'^dashboard/$', views.home, name = 'my_login_home'),
]

