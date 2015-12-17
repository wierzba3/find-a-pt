from django.shortcuts import render, get_object_or_404
from django.http import Http404

# Create your views here.
from trainer_app.models import TrainerProfile
from main_app.forms import SearchForm

def index(request):
	form = SearchForm()
	context = { 'form': form }
	return render(request, "main_app/index.html", context)
	

def trainer_profiles(request):
	"""
	A view that displays a set of TrainerProfile objects
	The result set is may be filtered by a SearchForm GET request
	"""
	context = {}
	trainer_list = None
	if (request.method == 'GET'):
		name_search = request.GET.get('name_search', None)
		if(name_search):
			context['name_search'] = name_search
			trainer_list = TrainerProfile.objects.filter(user__username__icontains=name_search)
		else:
			trainer_list = TrainerProfile.objects.all()
	context['trainer_list'] = trainer_list
	return render(request, "main_app/trainer_profiles.html", context)
	
def view_trainer(request, user_id):
	try:
		trainer = TrainerProfile.objects.get(user__pk=user_id)
	except TrainerProfile.DoesNotExist:
		raise Http404("Trainer profile does not exist")
	return render(request, "main_app/view_trainer.html", { 'trainer': trainer })
	
