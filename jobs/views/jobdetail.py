from django.urls import reverse_lazy
from django.views.generic import DetailView, UpdateView, DeleteView
from django.views import View
from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib import messages

from users.models import CustomUser
from ..models import Job, AppliedJobs

class JobDetailView(DetailView):
    model = Job
    template_name = 'jobs/jobdetail.html'
    context_object_name = 'job'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        user = self.request.user
        job = self.get_object()
        if user.is_authenticated:
            context['is_owner'] = (user.role == 'admin' and job.posted_by == user)
            context['has_applied'] = AppliedJobs.objects.filter(
                user=self.request.user,
                job=self.get_object()
            ).exists()

        return context


class ApplyJobView(LoginRequiredMixin, View):
    def post(self, request, pk):
        job = get_object_or_404(Job, pk=pk)

        if job.status == 'open':

            applied, created = AppliedJobs.objects.get_or_create(
                user=request.user,
                job=job
            )

            if created:
                messages.success(request, "Application submitted!")
            else:
                messages.info(request, "You've already applied for this.")
        else:
            messages.error(request, "This job is currently closed.")

        return redirect('jobs:job_detail', pk=pk)



class JobUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Job
    fields = ['title', 'company_name', 'min_salary', 'max_salary', 'status', 'description']
    template_name = 'jobs/addjob.html'

    def test_func(self):
        job = self.get_object()
        return self.request.user == job.posted_by

    def get_success_url(self):
        return reverse_lazy('jobs:job_detail', kwargs={'pk': self.object.pk})


class JobDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Job
    success_url = reverse_lazy('jobs:job_list')

    def test_func(self):
        job = self.get_object()
        return self.request.user == job.posted_by