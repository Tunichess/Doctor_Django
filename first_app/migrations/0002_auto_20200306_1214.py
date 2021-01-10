# Generated by Django 2.1.7 on 2020-03-06 11:14

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='personne',
            name='release_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 3, 6, 12, 14, 41, 212760)),
        ),
        migrations.AlterField(
            model_name='personne',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='score',
            name='first_name',
            field=models.CharField(max_length=256),
        ),
        migrations.AlterField(
            model_name='score',
            name='last_name',
            field=models.CharField(max_length=256),
        ),
        migrations.AlterField(
            model_name='score',
            name='personne',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='first_app.Personne'),
        ),
    ]
