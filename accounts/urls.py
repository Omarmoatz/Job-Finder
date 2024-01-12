from django.urls import path
from .views import signUp,activat,profile,edit_profile

app_name = 'accounts'

urlpatterns = [
    path('signup/', signUp, name='signup'),
    path('signup/activat', activat, name='signup_activate'),
    path('profile/', profile, name='profile'),
    path('profile/edit', edit_profile, name='profile_edit'),
]

