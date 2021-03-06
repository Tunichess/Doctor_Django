# Generated by Django 2.1.7 on 2020-02-25 14:06

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Personne',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=256)),
                ('last_name', models.CharField(max_length=256)),
                ('birthday', models.CharField(max_length=256)),
                ('state', models.CharField(choices=[('medecin', 'Medecin'), ('etudiant', 'Etudiant')], max_length=25)),
                ('release_date', models.DateTimeField(default=datetime.datetime(2020, 2, 25, 15, 6, 14, 48829))),
            ],
        ),
        migrations.CreateModel(
            name='Score',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(default='PERS', max_length=256)),
                ('last_name', models.CharField(default='PERS', max_length=256)),
                ('score', models.PositiveIntegerField()),
                ('resultat', models.CharField(max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name='Etudiant',
            fields=[
                ('personne_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='first_app.Personne')),
                ('Etablissement', models.CharField(max_length=256)),
                ('Niveau_d_etude', models.CharField(max_length=256)),
                ('Adresse', models.CharField(max_length=256)),
            ],
            bases=('first_app.personne',),
        ),
        migrations.CreateModel(
            name='Medecin',
            fields=[
                ('personne_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='first_app.Personne')),
                ('profession', models.CharField(max_length=256)),
                ('specialite', models.CharField(max_length=256)),
                ('Matricule', models.PositiveIntegerField()),
                ('Adresse', models.CharField(max_length=256)),
                ('Telephone', models.PositiveIntegerField()),
            ],
            bases=('first_app.personne',),
        ),
        migrations.AddField(
            model_name='score',
            name='personne',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='scores', to='first_app.Personne'),
        ),
        migrations.AddField(
            model_name='personne',
            name='user',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
