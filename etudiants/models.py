from django.db import models
from django.utils import timezone

class Etudiant(models.Model):
    FILIERES = [
        ('dsi', 'Dsi'),
        ('rss', 'Rss'),
        ('dwm', 'Dwm'),
    ]

    NIVEAUX = [
        ('licence1', 'Licence 1'),
        ('licence2', 'Licence 2'),
        ('licence3', 'Licence 3'),
        ('master1', 'Master 1'),
        ('master2', 'Master 2'),
    ]

    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    email = models.EmailField(unique=True, max_length=191)
    matricule = models.CharField(max_length=50, unique=True)
    photo = models.ImageField(upload_to='photos/')
    filiere = models.CharField(max_length=50, choices=FILIERES)
    niveau = models.CharField(max_length=50, choices=NIVEAUX)
    encodage = models.TextField()

    def __str__(self):
        return f"{self.nom} {self.prenom}"
    

class Utilisateur(models.Model):
    ROLE_CHOICES = (
        ('SUPER_ADMIN', 'Super Admin'),
        ('SCOLARITE', 'Scolarité'),
    )

    username = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=255)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)
    email = models.EmailField(unique=True, max_length=191)


    def __str__(self):
        return self.username
    






