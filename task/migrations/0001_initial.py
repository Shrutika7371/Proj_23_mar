# Generated by Django 3.1.7 on 2021-04-08 18:47

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('teams', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('task_name', models.CharField(default='newassignment', max_length=30, primary_key=True, serialize=False, unique=True)),
                ('task_details', models.CharField(blank=True, default='newassignment', max_length=30, null=True)),
                ('start_date', models.DateTimeField(auto_now_add=True, null=True)),
                ('end_date', models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True)),
                ('task_status', models.CharField(blank=True, default='pending', max_length=30, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('proj_name', models.CharField(default='newproj', max_length=200, primary_key=True, serialize=False, unique=True)),
                ('Proj_description', models.CharField(blank=True, default='description', max_length=500, null=True)),
                ('proj_status', models.CharField(blank=True, default='pending', max_length=100, null=True)),
                ('start_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('end_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('assigned_to', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='teams.team')),
            ],
        ),
    ]
