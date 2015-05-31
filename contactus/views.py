from django.shortcuts import render
from django.http import HttpResponse
from contactus.models import Supporter
import json


def supportus(request):
	c=Supporter(name=request.GET['name'])
	c.save()
	data={'error':0,'message':'Thank You'}
	success=json.dumps(data)
	return HttpResponse(success,content_type='application/json')

def getcount(request):
	count=len(Supporter.objects.all())
	data={'error':0,'count':count}
	count_data=json.dumps(data)
	return HttpResponse(count_data,content_type='application/json')
