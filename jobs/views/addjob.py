from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from jobs.forms import JobForm

@login_required
def add_job_view(request):
    if request.method == "POST":
        form = JobForm(request.POST)
        if form.is_valid():
            job = form.save(commit=False)
            job.posted_by = request.user
            job.company_name = getattr(request.user, 'company_name', 'Tech Company')
            job.save()
            return redirect('jobs:dashboard')
    else:
        form = JobForm()
    return render(request, 'jobs/addjob.html', {'form': form})