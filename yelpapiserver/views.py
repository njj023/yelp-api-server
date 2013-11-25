from django.http import HttpResponse
from django.db import connection
import datetime
import pdb
import httplib
import yelpapicaller
import json

def search(request):
	# change to POST
	if not request.method == 'GET' or \
			not 'q' in request.GET or \
			not 'l' in request.GET:
		return HttpResponse('Bad request',status = 400)

	search_params = [x.strip() for x in request.GET['q'].split(',')]
	location = request.GET['l'].strip()

	# for s in search_params:
	# 	print("Search Param = %s" %s)
	# print("Location = %s" %location)
	
	data = yelpapicaller.get_results(search_params, location)

	return HttpResponse(json.dumps(data))
