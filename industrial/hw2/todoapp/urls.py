from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('all/', views.TaskListView.as_view(), name='all'),
    path('done/', views.DoneTaskListView.as_view(), name='done'),
    path('pending/', views.PendingTaskListView.as_view(), name='pending'),
    path('task/(?P<pk>\d+)', views.TaskDetailView.as_view(), name='task-detail')
]
