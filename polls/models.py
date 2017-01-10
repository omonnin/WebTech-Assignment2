from django.db import models
from django.utils import timezone
from django.contrib import admin
# Create your models here.

#fairly self-explanatory, the voters field is used to establish who has already voted so that they may not vote twice
class Poll(models.Model):
	author = models.ForeignKey('auth.User', related_name='polls', on_delete=models.CASCADE)
	title = models.CharField(max_length=200, blank=False, unique=True)
	published_date = models.DateTimeField(default=timezone.now)
	voters = models.ManyToManyField('auth.User')
	multiple_answers = models.BooleanField(default = False)

	def __unicode__(self):
		return self.title
	
	def __str__(self):
		return self.title

#Each poll can have several answers which are found with the poll's unique id
class Answer(models.Model):
	poll = models.ForeignKey(Poll, related_name='answers', on_delete=models.CASCADE)
	description = models.CharField(max_length=100, blank=False)
	votes = models.IntegerField(default=0)
	
	def __str__(self):
		return self.description
	
	def __unicode__(self):
		return self.description