from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required(login_url='login')
def profile_view(request):
    user = request.user
    
    if request.method == 'POST':
       
        new_description = request.POST.get('description')
        user.description = new_description
        user.save()
        
        
    return render(request, 'users/profile.html', {'user': user})
