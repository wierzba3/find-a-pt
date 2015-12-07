from django.shortcuts import render

# Create your views here.
from trainer_app.models import TrainerProfile

def index(request):
	trainer_list = TrainerProfile.objects.all()
	context = { 'trainer_list': trainer_list }
	return render(request, 'main_app/index.html', context)
	#return render(request, 'main_app/index.html')
	
