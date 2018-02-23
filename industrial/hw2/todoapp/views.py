from django.shortcuts import render

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
