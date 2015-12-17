from django.db import models
from django.contrib.auth.models import User


class TrainerProfile(models.Model):
	user = models.OneToOneField(User, primary_key=True)
	bio = models.CharField(max_length=1024, default="No bio")
	education = models.CharField(max_length=256, default="Not specified")
	gender = models.CharField(max_length=64, default="Male")
	rate = models.CharField(max_length=256, default="Not specified")
	online_training = models.BooleanField(default=False)
	#Field for the trainer to specify other details about the locations they train out of
	trains_at = models.CharField(max_length=256, default="")
	
	def __str__(self):
		return self.bio


class SuccessStory(models.Model):
	profile = models.ForeignKey(TrainerProfile, on_delete=models.CASCADE)
	story_text = models.CharField(max_length=1024, default="")
	
	
class CertificationEnum(models.Model):
	"""
	A set of pre-defined Certification types
	"""
	certification_name = models.CharField(max_length=256)
class Certification(models.Model):
	"""
	A child record of TrainerProfile.
	A TrainerProfile record can specify 0 to many Certifications
	"""
	profile = models.ForeignKey(TrainerProfile, on_delete=models.CASCADE)
	#certification_name = models.CharField(max_length=256)
	certification_type = models.ForeignKey(CertificationEnum, null=True, on_delete=models.CASCADE)

	
class Specialty(models.Model):
	"""
	A child record of TrainerProfile
	A Specialty is linked to a client Goal type
	"""
	profile = models.ForeignKey(TrainerProfile, on_delete=models.CASCADE)
	specialty_type = models.ForeignKey('client_app.GoalEnum', on_delete=models.CASCADE)	
#class SpecialtyEnum(models.Model):
#	specialty_name = models.CharField(max_length=256)
	

class GymEnum(models.Model):
	"""
	A set of pre-defined gyms
	"""
	gym_name = models.CharField(max_length=256)
class Gym(models.Model):
	"""
	A child record of TrainerProfile.
	A TrainerProfile record can specify 0 to many gyms (that the trainer trains out of)
	"""
	profile = models.ForeignKey(TrainerProfile, on_delete=models.CASCADE)
	gym_type = models.ForeignKey(GymEnum, on_delete=models.CASCADE)

	
	
	

