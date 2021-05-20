from operator import mod
from django.shortcuts import render
from base.models import Tag, Task, Project
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin

class CustomLoginView(LoginView):
    template_name = 'base/login.html'
    fields = '__all__'
    redirect_authenticated_user = True
    
    def get_success_url(self):
        return reverse_lazy('boards')

class TaskList(ListView):
    model = Task
    context_object_name = 'tasks'
    template_name = 'base/boards.html'

class TaskCreate(LoginRequiredMixin ,CreateView):
    model = Task
    fields = ['assignees', 'title', 'description', 'priority', 'tag']
    success_url = reverse_lazy('boards')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(TaskCreate, self).form_valid(form)

class TaskUpdate(UpdateView):
    model = Task
    fields = ['assignees', 'title', 'description', 'priority', 'tag']
    success_url = reverse_lazy('boards')


