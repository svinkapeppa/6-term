from django.db import models
from django.urls import reverse


class Task(models.Model):
    """
    Model representing single task.
    """
    description = models.TextField(max_length=256, help_text="Describe your task here")
    additional_info = models.TextField(max_length=1024, help_text="Write some tips here")

    TASK_STATUS = (
        ('p', 'Pending'),
        ('d', 'Done')
    )

    status = models.CharField(max_length=1, choices=TASK_STATUS, default='p', help_text='Set status of the task')

    def __str__(self):
        """
        String for representing model object.
        """
        return self.description

    def get_absolute_url(self):
        return reverse('task-detail', args=[str(self.id)])
