from django.http import HttpResponse

def profile_view(request):
    return HttpResponse(f"Welcome to your profile, {request.user.fname}!")