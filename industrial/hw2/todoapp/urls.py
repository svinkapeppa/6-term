from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('all/', views.TaskByUserListView.as_view(), name='all'),
    path('done/', views.TaskDoneByUserListView.as_view(), name='done'),
    path('pending/', views.TaskPendingByUserListView.as_view(), name='pending'),
    path('task/(?P<pk>\d+)', views.TaskDetailView.as_view(), name='task-detail'),
    path('task/create/', views.TaskCreate.as_view(), name='task_create'),
    path('task/(?P<pk>\d+)/update/', views.TaskUpdate.as_view(), name='task_update'),
    path('task/(?P<pk>\d+)/delete/', views.TaskDelete.as_view(), name='task_delete'),
]
