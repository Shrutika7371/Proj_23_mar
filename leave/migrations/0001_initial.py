# Generated by Django 3.1.7 on 2021-04-03 08:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Leave',
            fields=[
                ('leave_req_id', models.AutoField(primary_key=True, serialize=False)),
                ('leave_reason', models.CharField(blank=True, default='personal reason', max_length=30, null=True)),
                ('start_date', models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True)),
                ('end_date', models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True)),
                ('no_of_days', models.IntegerField(default=0)),
                ('team_name', models.CharField(blank=True, default='none', max_length=30, null=True)),
                ('Leave_Status', models.CharField(default='pending', max_length=10)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]