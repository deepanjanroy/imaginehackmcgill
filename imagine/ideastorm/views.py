# Create your views here.

from django.shortcuts import render
from ideastorm.models import Idea
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.http import HttpResponse

def index(request):
    context = {}
    return render(request, 'ideastorm/index.html', context)

def idealist(request):
    context = {}
    if request.method == 'POST':

        Idea.objecdffdts.create(title=request.POST['title'],
                                       description=request.POST['description'])
        return render(request, 'ideastorm/index.html', context)

    if request.method == 'GET':
        return render(request, 'ideastorm/index.html', context)

def sample_login(request):
    context = {}
    if request.method == 'GET':
        return render(request, 'ideastorm/sample_login.html', context)

def current_user(request):
    print "Current user: " + str(request.user)
    return HttpResponse("I believe you're {0}".format(str(request.user.username)))

def sample_logout(request):
    context = {"social": request.user.social_auth.get()}
    if request.method == 'GET':
        return render(request, 'ideastorm/sample_logout.html', context)

def sample_logged_in(request):
    context = {"name": request.user.first_name}
    if request.method == 'GET':
        return render(request, 'ideastorm/sample_logged_in.html', context)

def imagine_login(request):
    context = {}
    if request.method == 'GET':
        return render(request, 'ideastorm/login.html', context)

    if request.method == 'POST':
        username= request.POST.get('email', None)
        password= request.POST.get('password', None)
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)

def signup(request):
    context = {}
    if request.method == 'GET':
        return render(request, 'ideastorm/signup.html', context)

    if request.method == 'POST':
        email= request.POST.get('email', None)
        password= request.POST.get('password', None)
        username= request.POST.get('username', None)
        if not username:
            username = email.split("@")[0] # Just get the first part of the email.

        if User.objects.filter(email=email).exists():
            print "Email already exists! Aborting. Mayhem. Disaster."
            return HttpResponse("Email already taken. :|")

        try:
            User.objects.create_user(username=username, password=password, email=email)
        except IntegrityError:
            return HttpResponse("Someone already stole your username. Sorry.")

        user = authenticate(username=username, password=password)
        login(request, user)
        return HttpResponse("Successfully registered! {0}, you're now logged in.".format(username))



