# Generated by Django 4.2.5 on 2023-09-14 21:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='task',
            old_name='task_date',
            new_name='due_date',
        ),
    ]