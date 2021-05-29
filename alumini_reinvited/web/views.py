from django.shortcuts import render

# Create your views here.

def home_view(request):
    context={}
    return render(request, 'web/main.html', context)

def profile_view(request):
    context={}
    return render(request, 'web/profile.html', context)