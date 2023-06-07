# Generated by Django 4.2.2 on 2023-06-07 09:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0005_alter_task_timestamp'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='Status',
            field=models.CharField(choices=[('OPEN', 'OPEN'), ('WORKING', 'WORKING'), ('DONE', 'DONE'), ('OVERDUE', 'OVERDUE')], default='OPEN', max_length=10),
        ),
    ]
