from django.urls import path
from .views.signup import signup_view
from .views.profile import profile_view # Assuming you'll have this

urlpatterns = [
    path('signup/', signup_view, name='signup'),
    path('profile/', profile_view, name='profile'),
]