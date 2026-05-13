# Create your models here.
from django.db import models
from django.conf import settings

class Job(models.Model):
    STATUS_CHOICES = [
        ('open', 'Open'),
        ('closed', 'Closed'),
    ]

    title = models.CharField(max_length=255)
    company_name = models.CharField(max_length=255)
    min_salary = models.IntegerField()
    max_salary = models.IntegerField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='open')
    experience_required = models.IntegerField()
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    description = models.TextField()
    posted_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title


class AppliedJobs(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    job = models.ForeignKey(Job, on_delete=models.CASCADE, related_name='applications')
    applied_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'job')

    def __str__(self):
        return f"{self.user.email} applied for {self.job.title}"
