from django.urls import path
from .views.signup import signup_view
from .views.profile import profile_view # Assuming you'll have this
from .views.login import login_view

urlpatterns = [
    path('login/', login_view.as_view(), name='login'),
    path('signup/', signup_view, name='signup'),
    path('profile/', profile_view, name='profile'),
]