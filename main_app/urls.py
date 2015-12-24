from django.conf.urls import url

from . import views

urlpatterns = [
	
	url(r'^$', views.index, name='index'),
	url(r'^view_trainer/(?P<user_id>[0-9]+)/$', views.view_trainer, name='view_trainer'),
	url(r'^trainer_profiles/$', views.trainer_profiles, name='trainer_profiles'),
	
	
	#url(r'^trainer_profiles/(?P<zipcode>[0-9]*)$', views.trainer_profiles_search, name='trainer_profiles'),
    #url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
	#url(r'^(?P<pk>[0-9]+)/results/$', views.ResultsView.as_view(), name='results'),
	#url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
	
]
