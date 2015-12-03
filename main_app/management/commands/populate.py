from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group

class Command(BaseCommand):
	args = ''
	help = 'Clears out the database and populates it with the default data.'

	def _create_tags(self):
		#clear out the groups table
		Group.objects.all().delete()
		
		#create user groups for trainer, client
		trainer_group = Group(name='trainer')
		trainer_group.save()
		client_group = Group(name='client')
		client_group.save()
		
        

	def handle(self, *args, **options):
		self._create_tags()
