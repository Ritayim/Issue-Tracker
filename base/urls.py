from django.conf.urls import url
from django.urls import path
from django.urls import path

from .views import ProjectCreate, ProjectTaskList, TaskCreate, CustomLoginView, TaskUpdate, ProjectList
from django.contrib.auth.views import LogoutView    

urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('', ProjectList.as_view(), name='projects'),
    path('project-create/', ProjectCreate.as_view(), name='project-create'),
    path('board/', ProjectTaskList.as_view(), name='board'),
    path('task-create/', TaskCreate.as_view(), name='task-create'),
    path('task-update/', TaskUpdate.as_view(), name='task-update'),
    
]
