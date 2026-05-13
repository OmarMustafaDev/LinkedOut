from django.urls import path
from .views.addjob import add_job_view
from .views.jobdetail import JobDetailView, ApplyJobView, JobUpdateView, JobDeleteView
from .views.joblist import job_list_view
from .views.dashboard import DashboardListView



app_name = 'jobs'

urlpatterns = [
    path('add/', add_job_view.as_view(), name='add_job'),
    path('list/', job_list_view.as_view(), name='job_list'),
    path('dashboard/', DashboardListView.as_view(), name='dashboard'),
    path('detail/<int:pk>/', JobDetailView.as_view(), name='job_detail'),
    path('apply/<int:pk>/', ApplyJobView.as_view(), name='apply_now'),
    path('detail/<int:pk>/edit/', JobUpdateView.as_view(), name='edit_job'),
    path('detail/<int:pk>/delete/', JobDeleteView.as_view(), name='delete_job'),
]