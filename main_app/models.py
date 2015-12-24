from django.db import models
from django.contrib.auth.models import User

from trainer_app.models import TrainerProfile
from client_app.models import ClientProfile

# Create your models here.
class UserProfile(models.Model):
	user = models.OneToOneField(User, primary_key=True)
	account_type = models.IntegerField(default=0)
	client_profile = models.OneToOneField(ClientProfile, default=None, blank=True, null=True)
	trainer_profile = models.OneToOneField(TrainerProfile, default=None, blank=True, null=True)
	
class AccountType:
	"""
	Constant values for the type of account
	"""
	TRAINER = 1
	CLIENT = 2

