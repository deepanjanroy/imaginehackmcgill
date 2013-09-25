# Create your views here.

from django.http import HttpResponse
from django.shortcuts import render
from ideastorm.models import Idea

def index(request):
    context = {}
    return render(request, 'ideastorm/index.html', context)

def idealist(request):
    if request.method == 'POST':
        new_idea = Idea.objects.create(title=request.POST['title'],
                                       description=request.POST['description'])

    # render_to_response()

    if request.method == 'GET':
        pass