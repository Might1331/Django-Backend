# Generated by Django 4.2.2 on 2023-06-07 08:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='Status',
            field=models.CharField(choices=[('OP', 'OPEN'), ('WO', 'WORKING'), ('DO', 'DONE'), ('OV', 'OVERDUE')], default='OP', max_length=10),
        ),
    ]
