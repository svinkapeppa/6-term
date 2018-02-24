from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView

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


class TaskDetailView(generic.DetailView):
    model = Task


class TaskByUserListView(LoginRequiredMixin, generic.ListView):
    model = Task
    template_name = 'todoapp/task_list_user.html'
    paginate_by = 10

    def get_queryset(self):
        return Task.objects.filter(creator=self.request.user)


class TaskDoneByUserListView(LoginRequiredMixin, generic.ListView):
    model = Task
    template_name = 'todoapp/task_done_list_user.html'
    paginate_by = 10

    def get_queryset(self):
        return Task.objects.filter(creator=self.request.user).filter(status__exact='d')


class TaskPendingByUserListView(LoginRequiredMixin, generic.ListView):
    model = Task
    template_name = 'todoapp/task_pending_list_user.html'
    paginate_by = 10

    def get_queryset(self):
        return Task.objects.filter(creator=self.request.user).filter(status__exact='p')


class TaskCreate(CreateView):
    model = Task
    fields = '__all__'
    initial = {'status': 'p', }


class TaskUpdate(UpdateView):
    model = Task
    fields = ['description', 'additional_info', 'status', 'creator']


class TaskDelete(DeleteView):
    model = Task
    success_url = reverse_lazy('index')
