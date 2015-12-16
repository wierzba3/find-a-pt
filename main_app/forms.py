from django import forms

class SearchForm(forms.Form):
	name_search = forms.CharField(max_length=64)
