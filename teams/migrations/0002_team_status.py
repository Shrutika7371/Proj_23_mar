# Generated by Django 3.1.7 on 2021-03-24 16:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teams', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='status',
            field=models.CharField(default='free', max_length=10),
        ),
    ]