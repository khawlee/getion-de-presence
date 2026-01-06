from django.db import models

class Etudiant(models.Model):
    FILIERES = [
        ('informatique', 'Informatique'),
        ('gestion', 'Gestion'),
        ('marketing', 'Marketing'),
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
    


class Presence(models.Model):
    etudiant = models.ForeignKey('Etudiant', on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)

    presence_debut = models.BooleanField(default=False)
    presence_fin = models.BooleanField(default=False)

    statut = models.CharField(
        max_length=10,
        choices=[('PRESENT', 'Présent'), ('ABSENT', 'Absent')],
        default='ABSENT'
    )

    class Meta:
        unique_together = ('etudiant', 'date')

    def calculer_statut(self):
        self.statut = 'PRESENT' if self.presence_debut and self.presence_fin else 'ABSENT'
