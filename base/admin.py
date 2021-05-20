from django.contrib import admin
from .models import Task, Tag, Project

admin.site.register(Tag)
admin.site.register(Project)
admin.site.register(Task)

