from django.contrib.auth.models import AbstractUser
from django.db import models
import uuid
from django.conf import settings

class Company(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=256)
    description = models.TextField()
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,  # references your custom User model
        on_delete=models.SET_NULL,  # or models.CASCADE, depending on your logic
        null=True,
        blank=True,
        related_name='companies_created'
    )
    
    
    def __str__(self):
        return self.name
    

class User(AbstractUser):
    JOB_SEEKER = 'job_seeker'
    JOB_POSTER = 'job_poster'
    USER_TYPE_CHOICES = [
        (JOB_SEEKER, 'Job Seeker'),
        (JOB_POSTER, 'Job Poster'),
    ]

    user_type = models.CharField(
        max_length=20,
        choices=USER_TYPE_CHOICES,
        default=JOB_SEEKER,
        help_text="Indicates if user is a job seeker or job poster"
    )

    def __str__(self):
        return f"{self.username} ({self.get_user_type_display()})"
    


class Job(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=256)
    description = models.TextField()
    company = models.ForeignKey(
        Company,
        on_delete=models.CASCADE,
        related_name='jobs',
    )
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=False,
        related_name='jobs_created'
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.title} at {self.company.name}"