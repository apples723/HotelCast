from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^$', views.index, name='home'),
	url(r'^search_show/$', views.search_show, name='search'), 
	url(r'^search_movie/$', views.search_movie, name='search'), 
	url(r'^show/?', views.show_info, name='show '), 
	url(r'^movie/?', views.movie_info, name='movie'), 
	url(r'^execute/$', views.write_command, name="execute"),
	url(r'^command/$', views.get_command, name="command"),
	url(r'^remote/?', views.remote, name="remote"),
]