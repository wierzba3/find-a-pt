from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group
from django.contrib.auth.models import User

from main_app.models import *
from trainer_app.models import *



class Command(BaseCommand):
	args = ''
	help = 'Populates the database'

	def _create_tags(self):
		
		#clear out the groups table
		
		#create user groups for trainer, client
		Group.objects.all().delete()
		trainer_group = Group(name='trainer')
		trainer_group.save()
		client_group = Group(name='client')
		client_group.save()
		
		User.objects.exclude(username = "admin").delete()
		allison_user = User.objects.create_user(username='Allison',email='abe@provider.com', password='Allison')
		bob_user = User.objects.create_user(username='Bob',email='bob@provider.com', password='Bob')
		carl_user = User.objects.create_user(username='Carl',email='carl@provider.com', password='Carl')
		dan_user = User.objects.create_user(username='Dan',email='dan@provider.com', password='Dan')
		
		UserProfile.objects.all().delete()
		allison_user_profile = UserProfile(user=allison_user)
		allison_user_profile.save()
		bob_user_profile = UserProfile(user=bob_user)
		bob_user_profile.save()
		carl_user_profile = UserProfile(user=carl_user)
		carl_user_profile.save()
		dan_user_profile = UserProfile(user=dan_user)
		dan_user_profile.save()
		
		TrainerProfile.objects.all().delete()
		allison_trainer_profile = TrainerProfile(bio="Hi I'm Allison")
		allison_trainer_profile.save()
		bob_trainer_profile = TrainerProfile(bio="Hi I'm Bob")
		bob_trainer_profile.save()
		carl_trainer_profile = TrainerProfile(bio="Hi I'm Carl")
		carl_trainer_profile.save()
		dan_trainer_profile = TrainerProfile(bio="Hi I'm Dan")
		dan_trainer_profile.save()	
		
		SuccessStory.objects.all().delete()
		bob_story1 = SuccessStory(profile=bob_profile, story_text="bob's client story 1")	
		bob_story1.save()
        

	def handle(self, *args, **options):
		self._create_tags()
