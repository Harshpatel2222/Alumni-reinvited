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