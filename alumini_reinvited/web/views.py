from django.shortcuts import render

# Create your views here.

def home_view(request):
    context={}
    return render(request, 'web/main.html', context)

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
    context={}
    return render(request, 'web/sign.html', context)

def team_view(request):
    context={}
    return render(request, 'web/team.html', context)