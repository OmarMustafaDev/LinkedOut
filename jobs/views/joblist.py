from django.shortcuts import render
from jobs.models import Job

def job_list_view(request):
    query = request.GET.get('search', '')
    jobs = Job.objects.all()
    
    if query:
        jobs = jobs.filter(title__icontains=query)
        
    return render(request, 'jobs/joblist.html', {
        'jobs': jobs,
        'query': query,
        'count': jobs.count()
    })