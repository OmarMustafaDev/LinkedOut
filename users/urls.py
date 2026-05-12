from django.urls import path
from .views.signup import signup_view
from .views.profile import profile_view # Assuming you'll have this
from .views.login import login_view
from .views.profile import profile_view
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('login/', login_view.as_view(), name='login'),
    path('signup/', signup_view, name='signup'),
    path('profile/', profile_view, name='profile'),
    path('logout/', auth_views.LogoutView.as_view(next_page='index'), name='logout'),
]