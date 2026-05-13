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
    
    def get_context_data(self, **kwargs):
        """Passes the search query and count back to the template."""
        context = super().get_context_data(**kwargs)
        
        search_term = self.request.GET.get('search', '')
        context['query'] = search_term
        
        context['count'] = self.get_queryset().count()
        
        return context