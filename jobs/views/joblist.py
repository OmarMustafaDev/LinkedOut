from django.views.generic import ListView
from jobs.models import Job

class job_list_view(ListView):
    model = Job
    template_name = 'jobs/joblist.html'
    context_object_name = 'jobs'
    
    def get_queryset(self):
        query = self.request.GET.get('search' , '')
        if query:
            return Job.objects.filter(title__icontains=query)
        return Job.objects.all()