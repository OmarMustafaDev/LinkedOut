from django.urls import path
from .views.signup import signup_view
from .views.profile import profile_view
from .views.login import login_view
from django.contrib.auth import logout
from django.shortcuts import redirect

def logout_view(request):
    logout(request)
    return redirect('/')

urlpatterns = [
    path('login/', login_view.as_view(), name='login'),  
    path('signup/', signup_view, name='signup'),
    path('profile/', profile_view, name='profile'),
    path('logout/', logout_view, name='logout'),  
]