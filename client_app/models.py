from django.db import models
from django.contrib.auth.models import User


class ClientProfile(models.Model):
	user = models.OneToOneField(User, primary_key=True)
	gender = models.CharField(max_length=64, default="Male")
	age = models.IntegerField(default=0)

	
class ExperienceEnum(models.Model):
	"""
	A set of pre-defined experience levels of the client
	Never, Long time ago, Semi regularly, Often
	"""
	experience_text = models.CharField(max_length=128)

class TrainingTypeEnum(models.Model):
	"""
	A set of pre-defined types of training (commercial gym, online training, any)
	"""
	training_type = models.CharField(max_length=128)

class Goals(models.Model):
	"""
	An object to encapsulate the goal criteria of a client
	"""
	client = models.OneToOneField(ClientProfile, primary_key=True)
	experience = models.ForeignKey(ExperienceEnum, null=True, on_delete=models.SET_NULL)
	training_type = models.ForeignKey(TrainingTypeEnum, null=True, on_delete=models.SET_NULL)
	other_details = models.CharField(max_length=512, default="")
	
	
class GoalEnum(models.Model):
	"""
	A set of pre-defined goals of the client
	Lose weight, gain strength, gain muscle, event preparation, rehab, general health
	"""
	goal_text = models.CharField(max_length=128)
class Goal(models.Model):
	"""
	A child record of Goals.
	A Goals record has 1 to many Goal type records
	"""
	goals = models.ForeignKey(Goals, on_delete=models.CASCADE)
	goal_type = models.ForeignKey(GoalEnum, on_delete=models.CASCADE)
	
	
class TrainingTimeEnum(models.Model):
	"""
	A set of pre-defined trainig times.
	Ex: Early morning, Late morning, Early afternoon, Late afternoon, Evening
	"""
	training_time = models.CharField(max_length=128)
class TrainingTime(models.Model):
	"""
	A child record of Goals.
	A Goals record has 1 to many TrainingTime records
	"""
	goals = models.ForeignKey(Goals, on_delete=models.CASCADE)
	training_time_type = models.ForeignKey(TrainingTimeEnum, on_delete=models.CASCADE)
	

