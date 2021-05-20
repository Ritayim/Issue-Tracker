from django.conf.urls import url
from django.urls import path
from django.urls import path

from .views import TaskList, TaskCreate, CustomLoginView, TaskUpdate
from django.contrib.auth.views import LogoutView    

urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('', TaskList.as_view(), name='boards'),
    path('task-create/', TaskCreate.as_view(), name='task-create'),
    path('task-update/', TaskUpdate.as_view(), name='task-update'),
    
]