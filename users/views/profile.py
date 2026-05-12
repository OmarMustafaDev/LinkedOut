from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required(login_url='login')
def profile_view(request):
    user = request.user
    
    if request.method == 'POST':
        # Grab the text from the textarea
        new_description = request.POST.get('description')
        user.description = new_description
        user.save()
        # You could add a success message here!
        
    return render(request, 'users/profile.html', {'user': user})