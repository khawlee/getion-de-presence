from django.db import models

class Etudiant(models.Model):
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    email = models.EmailField(unique=True, max_length=191)  # <-- 191 max pour MySQL
    photo = models.ImageField(upload_to='photos/')
    encodage = models.TextField()  # stockera le vecteur encodé du visage

    def __str__(self):
        return f"{self.nom} {self.prenom}"
