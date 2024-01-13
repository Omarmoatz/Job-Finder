from django.shortcuts import render,redirect
from .models import Profile,User
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
                f"Welcome {username} Use This Code :{profile.code} To Activate Your Account",
                "JopFinder@gmail.com",
                [email],
                fail_silently=False,
            )
            return redirect(f'/accounts/signup/{username}/activate')
    else:
        signupForm = SignUpForm()
    return render(request,'registration/signup.html',{'form':signupForm})

def activate(request,username):
    profile = Profile.objects.get(user__username=username)
    if request.method == 'POST':
        activationForm = ActivationForm(request.POST)
        if activationForm.is_valid():
            code = activationForm.cleaned_data['code']
            if code == profile.code:

                # to make the user login to page after useing code
                user = User.objects.get(username=profile.user.username)
                user.is_active = True
                user.save()

                profile.code = ''
                profile.save()
                return redirect('/accounts/login/')
    else:
        activationForm = ActivationForm()

    return render(request,'registration/activation.html',{'form':activationForm})



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
            return redirect('/accounts/profile')
    else:
        user_form = UserForm(instance=request.user)
        profile_form = ProfileForm(instance=profile)

    return render(request, 'accounts/profile_edit.html', {
        'user_form':user_form,
        'profile_form':profile_form,
    })


