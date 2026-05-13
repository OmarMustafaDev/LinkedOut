from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from ..models import AppliedJobs

class AppliedJobsListView(LoginRequiredMixin, ListView):
    template_name = "jobs/appliedjobs.html"
    context_object_name = "applied_jobs" 
    
    def get_queryset(self):
        return AppliedJobs.objects.filter(user=self.request.user).select_related('job').order_by('-applied_at')
    