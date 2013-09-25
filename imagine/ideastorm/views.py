# Create your views here.

from django.http import HttpResponse

def idealist(request):
	return HttpResponse("Hey world")