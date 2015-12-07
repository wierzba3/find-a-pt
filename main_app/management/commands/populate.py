from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group
from django.contrib.auth.models import User
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
		allison = User.objects.create_user(username='Allison',email='abe@provider.com', password='Abe')
		bob = User.objects.create_user(username='Bob',email='bob@provider.com', password='Bob')
		carl = User.objects.create_user(username='Carl',email='carl@provider.com', password='Carl')
		dan = User.objects.create_user(username='Dan',email='dan@provider.com', password='Dan')
		
		TrainerProfile.objects.all().delete()
		allison_profile = TrainerProfile(user=allison, bio="Hi I'm Allison")
		allison_profile.save()
		bob_profile = TrainerProfile(user=bob, bio="Hi I'm Bob")
		bob_profile.save()
		carl_profile = TrainerProfile(user=carl, bio="Hi I'm Carl")
		carl_profile.save()
		dan_profile = TrainerProfile(user=dan, bio="Hi I'm Dan")
		dan_profile.save()	
		
		SuccessStory.objects.all().delete()
		bob_story1 = SuccessStory(profile=bob_profile, story_text="bob's client story 1")	
		bob_story1.save()
        

	def handle(self, *args, **options):
		self._create_tags()
