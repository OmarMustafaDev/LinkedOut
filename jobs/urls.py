from django.urls import path
from .views.addjob import add_job_view
from .views.joblist import job_list_view

app_name = 'jobs'

urlpatterns = [
    path('add/', add_job_view, name='add_job'),
    path('list/', job_list_view, name='job_list'),
    path('detail/<int:pk>/', job_list_view, name='job_detail'),
    path('dashboard/', job_list_view, name='dashboard'),
]