from operator import mod
from django.shortcuts import render
from base.models import Tag, Task, Project
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic import DetailView
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin

class CustomLoginView(LoginView):
    template_name = 'base/login.html'
    fields = '__all__'
    redirect_authenticated_user = True
    
    def get_success_url(self):
        return reverse_lazy('board')

class ProjectList(LoginRequiredMixin, ListView):
    login_url = '/login/'
    model = Project
    context_object_name = 'projects'
    template_name = 'base/projects.html'

class ProjectCreate(CreateView):
    model = Project
    fields = ['name', 'members']
    success_url = reverse_lazy('projects')

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super(ProjectCreate, self).form_valid(form)

class ProjectTaskList(ListView):
    model = Project
    template_name = 'base/board.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['task_list'] = Task.objects.all()
        return context

class TaskCreate(CreateView):
    model = Task
    fields = ['assignees', 'title', 'description', 'priority', 'tag']
    success_url = reverse_lazy('board')

    def form_valid(self, form):
        form.instance.author = self.request.user
        project_id = self.request.GET.get('p')
        form.instance.project = Project.objects.get(id = project_id)
        return super(TaskCreate, self).form_valid(form)

class TaskUpdate(UpdateView):
    model = Task
    fields = ['assignees', 'title', 'description', 'priority', 'tag']
    success_url = reverse_lazy('board')



