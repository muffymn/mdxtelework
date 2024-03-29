from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class TeleworkRequest(models.Model):
    STATUS_CHOICES = (
        ('pending', 'Pending'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected'),
    )
    
    BENCH_CHOICES = (
        ('bench1', 'Bench 1'),
        ('bench2', 'Bench 2'),
        ('bench3', 'Bench 3'),
        ('other', 'Other'),
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    #file = models.FileField(upload_to='documents/')
    completion_date = models.DateField()
    completion_report = models.JSONField()
    date_requested = models.DateField()
    bench_assigned = models.CharField(max_length=100, choices=BENCH_CHOICES)
    other_bench_reason = models.TextField(blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')

    def save(self, *args, **kwargs):
        if self.bench_assigned != 'other':
            self.other_bench_reason = ''  # Reset other_bench_reason if bench_assigned is not 'other'
        super(TeleworkRequest, self).save(*args, **kwargs)

    def __str__(self):
        return f"{self.user.username} requests telework on {self.date_requested}"

#class TimeBlock(models.Model):
    #completion_report = models.ForeignKey('CompletionReport', on_delete=models.CASCADE, related_name='time_blocks')
    #start_time = models.TimeField()
    #end_time = models.TimeField()
    #task = models.CharField(max_length=200)

#class CompletionReport(models.Model):
    #user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name='completion_reports')
    #file = models.FileField(upload_to='documents/')
    #completion_date = models.DateField()
    #remarks = models.TextField()

    #def __str__(self):
        #return f"Completion report for {self.user.username} on {self.completion_date}"

#class TeleworkRequest(models.Model):
    #STATUS_CHOICES = (
        #('pending', 'Pending'),
        #('approved', 'Approved'),
        #('rejected', 'Rejected'),
    #)

    #user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name='telework_requests')
    #date_requested = models.DateField()
    #bench_assigned = models.CharField(max_length=100, choices=[
        #('bench1', 'Bench 1'),
        #('bench2', 'Bench 2'),
        #('bench3', 'Bench 3'),
        #('other', 'Other'),
    #])
    #other_bench_reason = models.TextField(blank=True)
    #status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')

    #completion_report = models.OneToOneField(CompletionReport, on_delete=models.CASCADE, null=True, blank=True)

    

    

