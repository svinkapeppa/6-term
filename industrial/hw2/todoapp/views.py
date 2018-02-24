from django.shortcuts import render
from django.views import generic

from .models import Task


def index(request):
    """
    Function to display home page.
    """
    num_tasks = Task.objects.all().count()
    num_done_tasks = Task.objects.filter(status__exact='d').count()
    num_pending_tasks = Task.objects.filter(status__exact='p').count()

    return render(
        request,
        'index.html',
        context={'num_tasks': num_tasks,
                 'num_done_tasks': num_done_tasks,
                 'num_pending_tasks': num_pending_tasks},
    )


class TaskListView(generic.ListView):
    model = Task
    paginate_by = 10


class TaskDetailView(generic.DetailView):
    model = Task


class DoneTaskListView(generic.ListView):
    model = Task
    paginate_by = 10

    @staticmethod
    def get_queryset():
        return Task.objects.filter(status__exact='d')


class PendingTaskListView(generic.ListView):
    model = Task
    paginate_by = 10

    @staticmethod
    def get_queryset():
        return Task.objects.filter(status__exact='p')
