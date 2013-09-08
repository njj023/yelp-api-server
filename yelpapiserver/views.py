from django.http import HttpResponse

def home(request):
	return HttpResponse("Hello and hi World!!")