from django.shortcuts import render, get_object_or_404
from django.http import Http404

# Create your views here.
from trainer_app.models import TrainerProfile

def index(request):

	return render(request, "main_app/index.html")
	
def trainer_profiles(request):
	trainer_list = TrainerProfile.objects.all()
	context = { 'trainer_list': trainer_list, 'x':'1' }
	return render(request, "main_app/trainer_profiles.html", context)
	
def trainer_profiles_search(request, zipcode):
	trainer_list = TrainerProfile.objects.all()
	context = { 'trainer_list': trainer_list, 'zipcode': zipcode, 'x':'2' }
	return render(request, "main_app/trainer_profiles.html", context)
	
def view_trainer(request, user_id):
	try:
		trainer = TrainerProfile.objects.get(user__pk=user_id)
	except TrainerProfile.DoesNotExist:
		raise Http404("Trainer profile does not exist")
	return render(request, "main_app/view_trainer.html", { 'trainer': trainer })
	
