from django.contrib import admin
from .models import Job, AppliedJobs

# Register your models here.
admin.site.register(Job)
class JobAdmin(admin.ModelAdmin):
    list_display = ('title', 'company_name', 'posted_by', 'created_at')


@admin.register(AppliedJobs)
class AppliedJobsAdmin(admin.ModelAdmin):
    # This makes the date appear in the list view
    list_display = ('user', 'job', 'applied_at')

    # This makes it appear inside the specific application page
    readonly_fields = ('applied_at',)