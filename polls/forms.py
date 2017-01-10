from django import forms
from .models import Poll, Answer

class PollForm(forms.ModelForm):
	class Meta:
		model = Poll
		fields = ('title',)

class AnswerForm(forms.ModelForm):
	class Meta:
		model = Answer
		fields = ('description',)
