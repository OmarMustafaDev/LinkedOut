from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib import messages
from ..forms import SignUpForm 

def signup_view(request):
    if request.method == 'POST':
        # it calls the form to validate the request
        form = SignUpForm(request.POST)
        if form.is_valid():
            # save the user to the database
            user = form.save()
            
            # log the user in after saving the data
            login(request, user)
            
            messages.success(request, "Registration successful!")
            return redirect('profile') # redirect to the profile page
        else:
            messages.error(request, "Unsuccessful registration. Invalid information.")
    else:
        # get request, provide empty form
        form = SignUpForm()
    
    return render(request, 'users/signup.html', {'form': form})