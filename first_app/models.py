from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import *

# Create your models here.
STATE= (
    ('medecin','Medecin'),
    ('etudiant','Etudiant'),)

TYPE= (
    ('radio ','Radio'),
    ('checkbox','Checkbox'),)

class Personne(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE,unique=True)
    first_name= models.CharField(max_length=256)
    last_name =models.CharField(max_length=256)
    birthday  =models.CharField(max_length=256)
    state = models.CharField(max_length=25,choices=STATE)
    release_date = models.DateTimeField(default=datetime.now())

    def __str__(self):
        return self.first_name, self.last_name
    def get_absolute_url(self):
        return reverse("first_app:detail",kwargs={'pk':self.pk})

class Medecin(Personne):
    profession= models.CharField(max_length=256)
    specialite= models.CharField(max_length=256)
    Matricule= models.PositiveIntegerField()
    Adresse=models.CharField(max_length=256)
    Telephone=models.PositiveIntegerField()

class Etudiant(Personne):
    Etablissement= models.CharField(max_length=256)
    Niveau_d_etude= models.CharField(max_length=256)
    Adresse=models.CharField(max_length=256)

class Score(models.Model):
    first_name= models.CharField(max_length=256)
    last_name =models.CharField(max_length=256)
    score = models.PositiveIntegerField()
    resultat=models.CharField(max_length=256)
    personne=models.OneToOneField(Personne, on_delete=models.CASCADE,unique=True)
    def __str__(self):
        return self.score

class questions(models.Model):
    Name= models.CharField(max_length=256)
    desciption=models.CharField(max_length=256)
    quest_date = models.DateTimeField(default=datetime.now())
    personne=models.OneToOneField(Personne, on_delete=models.CASCADE,unique=True)
    

class question(models.Model):
    quest= models.CharField(max_length=256)
    questtype=models.CharField(max_length=25,choices=TYPE)
    answer = models.CharField(max_length=256)
    scoreanswer=models.PositiveIntegerField()
    questions = models.ForeignKey(questions, on_delete=models.CASCADE,unique=True)


    