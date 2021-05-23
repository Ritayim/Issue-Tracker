from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE
from django.utils import timezone


class Project(models.Model):
    name = models.CharField(max_length=50)
    owner = models.ForeignKey(User, on_delete=models.PROTECT, related_name="owned_projects")
    members = models.ManyToManyField(User, related_name="projects")

class Tag(models.Model):
    project = models.ForeignKey("Project", related_name="tags", on_delete=models.CASCADE, default="")
    tag = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.tag}"

class Task(models.Model):
    LOW = 'L'
    MEDIUM = 'M'
    HIGH = 'H'
    PRIORITY_CHOICES = [
        (LOW, 'Low'),
        (MEDIUM, 'Medium'),
        (HIGH, 'High')
    ]

    author = models.ForeignKey(User, on_delete=models.CASCADE, null=False, blank=False)
    project = models.ForeignKey("Project", on_delete=models.CASCADE, related_name="tasks", null=False, blank=False)
    assignees = models.ManyToManyField(User, related_name="tasks", blank=True)
    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    priority = models.CharField(max_length=1, choices=PRIORITY_CHOICES)
    completion = models.BooleanField(default=False)
    tag = models.ManyToManyField(Tag, blank=True, related_name="tasks")
    dateTime = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.id} - {self.title} - {self.description} - {self.priority}"


    

