from django.contrib import admin
from trainer_app.models import *
# Register your models here.

class SuccessStoryInline(admin.StackedInline):
	model = SuccessStory
	extra = 0

class TrainerProfileAdmin(admin.ModelAdmin):
	inlines = [SuccessStoryInline]
	pass

admin.site.register(TrainerProfile, TrainerProfileAdmin)
