from django.urls import path
from .views.addjob import add_job_view
from .views.joblist import job_list_view
from .views.dashboard import DashboardListView

app_name = 'jobs'

urlpatterns = [

    path('add/', add_job_view.as_view(), name='add_job'),
    path('list/', job_list_view.as_view(), name='job_list'),
    path('detail/<int:pk>/', job_list_view.as_view(), name='job_detail'),
    path('dashboard/', DashboardListView.as_view(), name='dashboard'),
]