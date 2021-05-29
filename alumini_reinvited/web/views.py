from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth import authenticate, login, logout

from django.contrib import messages

from django.contrib.auth.decorators import login_required

# Create your views here.
from .models import *
from .forms import CreateUserForm


def home_view(request):
    context={}
    return render(request, 'web/main.html', context)

@login_required(login_url='sign_view')
def profile_view(request):
    context={}
    return render(request, 'web/profile.html', context)

def connections_view(request):
    context={}
    return render(request, 'web/connections.html', context)

def events_view(request):
    context={}
    return render(request, 'web/events.html', context)

def jobs_view(request):
    context={}
    return render(request, 'web/jobs.html', context)

def contact_view(request):
    context={}
    return render(request, 'web/contact.html', context)

def sign_view(request):
	if request.user.is_authenticated:
		return redirect('home_view')
	else:
		if request.method == 'POST':
			username = request.POST.get('username')
			password =request.POST.get('password')

			user = authenticate(request, username=username, password=password)

			if user is not None:
				login(request, user)
				return redirect('home_view')
			else:
				messages.info(request, 'Username OR password is incorrect')

		context = {}
		return render(request, 'web/signin.html', context)


def register_view(request):
	if request.user.is_authenticated:
		return redirect('home_view')
	else:
		form = CreateUserForm()
		if request.method == 'POST':
			form = CreateUserForm(request.POST)
			if form.is_valid():
				form.save()
				user = form.cleaned_data.get('username')
				messages.success(request, 'Account was created for ' + user)

				return redirect('sign_view')
			

		context = {'form':form}
		return render(request, 'web/register.html', context)

def logoutUser(request):
	logout(request)
	return redirect('login')

def team_view(request):
    context={}
    return render(request, 'web/team.html', context)