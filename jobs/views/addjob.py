from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from jobs.models import Job
from jobs.forms import JobForm

class add_job_view(CreateView):
    model = Job
    form_class = JobForm
    template_name = 'jobs/addjob.html'
    success_url = reverse_lazy('jobs:job_list')

    def form_valid(self, form):
        form.instance.posted_by = self.request.user 
        form.instance.company_name = self.request.user.company_name
        return super().form_valid(form)