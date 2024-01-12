from django.shortcuts import render
from .models import Profile


def signUp(request):
    return


def activat(request):
    return


def profile(request):
    profile = Profile.objects.get(user=request.user)
    return render(request, 'profile.html',{"profile": profile,})


