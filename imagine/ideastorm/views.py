# Create your views here.

from django.shortcuts import render
from ideastorm.models import Idea

def index(request):
    context = {}
    return render(request, 'ideastorm/index.html', context)

def idealist(request):
    if request.method == 'POST':
        context = {}
        Idea.objects.create(title=request.POST['title'],
                                       description=request.POST['description'])
        return render(request, 'ideastorm/index.html', context)

    if request.method == 'GET':
        return render(request, 'ideastorm/index.html', context)
