from django.shortcuts import render,redirect
from .models import Profile
from .forms import ProfileForm,UserForm,SignUpForm,ActivationForm

from django.core.mail import send_mail


def signUp(request):
    if request.method == 'POST':
        signupForm = SignUpForm(request.POST)
        if signupForm.is_valid():
            username = signupForm.cleaned_data['username']
            email = signupForm.cleaned_data['email']
            
            # to prevent the user from logining to page without the code
            form = signupForm.save(commit=False)
            form.is_active = False
            form.save()

            profile = Profile.objects.get(user__username=username)
            send_mail(
                "Activation Code",
                f"Welcome {username} Use This Code :{profile.code}",
                "JopFinder@gmail.com",
                [email],
                fail_silently=False,
            )
            return redirect(f'/registration/{username}/activate')
    else:
        signupForm = SignUpForm()
    return render(request,'registration/signup.html',{'form':signupForm})

def activate(request):
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


