# Generated by Django 4.2.2 on 2023-06-07 08:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0002_alter_task_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='Description',
        ),
        migrations.RemoveField(
            model_name='task',
            name='Due_date',
        ),
        migrations.RemoveField(
            model_name='task',
            name='Status',
        ),
        migrations.RemoveField(
            model_name='task',
            name='Tags',
        ),
    ]
