# Generated by Django 2.0.2 on 2018-02-23 15:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='status',
            field=models.CharField(choices=[('p', 'Pending'), ('d', 'Done')], default='p', help_text='Set status of the task', max_length=1),
        ),
    ]
