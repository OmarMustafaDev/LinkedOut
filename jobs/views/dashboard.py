from django.views.generic import ListView
from ..models import Job

class DashboardListView(ListView):
    model = Job
    template_name = "jobs/dashboard.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["jobs"] = Job.objects.filter(posted_by = self.request.user)
        return context
    
