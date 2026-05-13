from django.urls import path
from .views.addjob import add_job_view
from .views.jobdetail import JobDetailView, ApplyJobView, JobUpdateView, JobDeleteView
from .views.joblist import job_list_view



app_name = 'jobs'

urlpatterns = [
    path('add/', add_job_view.as_view(), name='add_job'),
    path('list/', job_list_view.as_view(), name='job_list'),
    path('detail/<int:pk>/', JobDetailView.as_view(), name='job_detail'),
    path('dashboard/', job_list_view.as_view(), name='dashboard'),
    path('apply/<int:pk>/', ApplyJobView.as_view(), name='apply_now'),
    path('detail/<int:pk>/edit/', JobUpdateView.as_view(), name='edit_job'),
    path('detail/<int:pk>/delete/', JobDeleteView.as_view(), name='delete_job'),
]