from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^add_travel$', views.new, name="add_travel"),
	url(r'^show_travel/(?P<id>\d+)$', views.show, name="show_plan"),
	url(r'^join/(?P<id>\d+)$', views.join, name="join"),
	url(r'^create$', views.create, name="create_trip"),
]
