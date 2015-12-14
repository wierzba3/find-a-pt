from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class TrainerProfile(models.Model):
	user = models.OneToOneField(User, primary_key=True)
	bio = models.CharField(max_length=1024, default="")
	
	def __str__(self):
		return self.bio

class SuccessStory(models.Model):
	profile = models.ForeignKey(TrainerProfile, on_delete=models.CASCADE)
	story_text = models.CharField(max_length=1024, default="")
	
class Certification(models.Model):
	profile = models.ForeignKey(TrainerProfile, on_delete=models.CASCADE)
	certification_name = models.CharField(max_length=256)
	
class SpecialtyType(models.Model):
	specialty_name = models.CharField(max_length=256)
	
class Specialty(models.Model):
	profile = models.ForeignKey(TrainerProfile, on_delete=models.CASCADE)
	specialty_type = models.ForeignKey(SpecialtyType, on_delete=models.CASCADE)
	
	

