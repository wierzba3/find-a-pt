from django.conf.urls import url

from . import views

urlpatterns = [
	
	url(r'^$', views.index, name='index'), #change this to be 
	url(r'^trainer_profiles/$', views.trainer_profiles, name='trainer_profiles'),
    #url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
	#url(r'^(?P<pk>[0-9]+)/results/$', views.ResultsView.as_view(), name='results'),
	#url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
	
]