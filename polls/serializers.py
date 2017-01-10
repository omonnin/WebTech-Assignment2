from rest_framework import serializers
from .models import Poll, Answer
from django.contrib.auth.models import User
from django.utils import timezone

'''class UserSerializer(serializers.ModelSerializer):
	class Meta:
		model = User
		fields = ('id')'''

class PollSerializer(serializers.ModelSerializer):
	class Meta:
		model = Poll
		fields = ('author', 'title', 'published_date')

class AnswerSerializer(serializers.ModelSerializer):
	class Meta:
		model = Answer
		fields = ('poll', 'description', 'votes')