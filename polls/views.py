from django.shortcuts import render, redirect, get_object_or_404
from .models import Poll, Answer
from .forms import PollForm, AnswerForm
from .serializers import PollSerializer, AnswerSerializer
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, Http404
from rest_framework.response import Response
from rest_framework.views import APIView

# These view generate pages.
@login_required
def add_poll(request):

	if request.method == "POST":	#if a request is sent
		pform = PollForm(request.POST, instance=Poll())		#store all request data in objects
		aforms = [AnswerForm(request.POST, prefix=str(x), instance=Answer()) for x in range(0,3)]
		if pform.is_valid() and all([af.is_valid() for af in aforms]):	#then establish validity
			new_poll = pform.save(commit=False)	#create a new poll
			new_poll.author = request.user
			new_poll.save()
			for af in aforms:
				new_answer = af.save(commit=False)
				new_answer.poll = new_poll
				new_answer.save()	#then create all new answers and attach them to the poll
			return redirect('/polls/')
	else:
		pform = PollForm(instance=Poll())
		aforms = [AnswerForm(prefix=str(x), instance=Answer()) for x in range(0,3)]
	return render(request, 'polls/add_poll.html', {'poll_form': pform, 'answer_forms': aforms})

def poll_detail(request, pk):
	poll = get_object_or_404(Poll, pk=pk)
	try:
		vote = poll.answers.get(pk=request.POST['answer'])
	except (KeyError, Answer.DoesNotExist):
		return render(request, 'polls/poll_detail.html', {'pk': poll.pk, 'poll': poll, 'error_message':'Please choose an answer'})
	else:
		if(poll.voters.get(id = request.user.id) is not None):
			return render(request, 'polls/poll_detail.html', {'pk': poll.pk, 'poll': poll, 'error_message':'You have already voted'})
		vote.votes = vote.votes + 1
		vote.save()
		poll.voters.add(request.user)
		poll.save()
		return render(request, 'polls/poll_detail.html', {'poll': poll, 'pk': poll.pk})
		
# These views generate API requests

class APIPollSingle(APIView):
	def get_object(self, pk):
		try:
			return Poll.objects.get(pk=pk)
		except Question.DoesNotExist:
			raise Http404

	def get(self, request, pk, format=None):
		poll = self.get_object(pk)
		serializer = PollSerializer(poll)
		return Response(serializer.data)

	def put(self, request, pk, format=None):
		poll = self.get_object(pk)
		serializer = PollSerializer(poll, data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

	def delete(self, request, pk, format=None):
		poll = self.get_object(pk)
		poll.delete()
		return Response(status=status.HTTP_204_NO_CONTENT)

class APIAnswerSingle(APIView):
    def get_object(self, pk):
        try:
            return Answer.objects.get(pk=pk)
        except Answer.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        answer = self.get_object(pk)
        serializer = AnswerSerializer(answer)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        answer = self.get_object(pk)
        serializer = AnswerSerializer(answer, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        answer = self.get_object(pk)
        answer.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)