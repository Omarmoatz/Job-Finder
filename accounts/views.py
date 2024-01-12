from django.shortcuts import render
from .models import Profile
from .forms import ProfileForm,UserForm


def signUp(request):
    return


def activat(request):
    return


def profile(request):
    profile = Profile.objects.get(user=request.user)
    return render(request, 'accounts/profile.html',{"profile": profile,})

def edit_profile(request):
    profile = Profile.objects.get(user=request.user)

    if request.method == 'POST':
        user_form = UserForm(request.POST,instance=request.user)
        profile_form = ProfileForm(request.POST,request.FILES,instance=profile)
        if user_form.is_valid and profile_form.is_valid:
            user_form.save()
            myProfile = profile_form.save(commit=False)
            myProfile.user = request.user
            myProfile.save()
    else:
        user_form = UserForm(instance=request.user)
        profile_form = ProfileForm(instance=profile)

    return render(request, 'accounts/profile_edit.html', {
        'user_form':user_form,
        'profile_form':profile_form,
    })


