from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^polls/$', views.add_poll, name='add_poll'),
	url(r'^poll/(?P<pk>\d+)/$', views.poll_detail, name='poll_detail'),
	url(r'^api/poll/(?P<pk>\d+)$', views.APIPollSingle.as_view(), name='poll_single'),
	url(r'^api/answer/(?P<pk>\d+)$', views.APIAnswerSingle.as_view(), name='answer_single'),
]