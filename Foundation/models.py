from django.db import models
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFit

class Adherant(models.Model):
    nom = models.CharField(max_length=30)
    post_nom = models.CharField(max_length=30)
    prenom = models.CharField(max_length=30)
    telephone = models.CharField(max_length=15)
    genre = models.CharField(max_length=1)
    lieu_de_naissance = models.CharField(max_length=100) 
    date_de_naissance = models.DateField()
    adresse = models.CharField(max_length=100)  # Augmenté à 100 caractères pour plus de flexibilité
    pays = models.CharField(max_length=40)
    ville = models.CharField(max_length=30)  # Augmenté à 30 caractères pour plus de flexibilité
    businessName = models.CharField(max_length=100)  # Augmenté à 100 caractères pour plus de flexibilité
    legalForm = models.CharField(max_length=30)  # Utilisation de legalForm en minuscules
    actif = models.BooleanField(default=False)
    def __str__(self):
        return f"{self.nom} {self.prenom}"

class Ambassadeur(models.Model):
    nom = models.CharField(max_length=30)
    prenom = models.CharField(max_length=30)
    telephone = models.CharField(max_length=15)
    pays = models.CharField(max_length=40)
    ville = models.CharField(max_length=30)  # Augmenté à 30 caractères pour plus de flexibilité
    profession = models.CharField(max_length=50)
    email = models.EmailField(max_length=255)  # Utilisation de EmailField pour l'email
    raison = models.CharField(max_length=255)
    profil = ProcessedImageField(upload_to='ambassadeurs/',
                                 processors=[ResizeToFit(width=300, height=300)],
                                 format='JPEG',
                                 options={'quality': 90})
  # Exemple de chemin de téléchargement pour les images
    instagram = models.CharField(max_length=30, blank=True, null=True)
    facebook = models.CharField(max_length=30, blank=True, null=True)
    linkedin = models.CharField(max_length=30, blank=True, null=True)
    youtube = models.CharField(max_length=30, blank=True, null=True)
    actif = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.prenom} {self.nom}"

class Histoire(models.Model):
    nom = models.CharField(max_length=30)
    prenom = models.CharField(max_length=30)
    email = models.EmailField(max_length=255)
    telephone = models.CharField(max_length=50)
    stories = models.CharField(max_length=255)
    etat = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.prenom} {self.nom}"

class Evenement(models.Model):
    nom = models.CharField(max_length=30)
    date_de_debut = models.DateField()
    date_de_fin = models.DateField()
    description = models.CharField(max_length=255)
    lieu = models.CharField(max_length=100)
    cible = models.CharField(max_length=100)
    budget = models.DecimalField(max_digits=10, decimal_places=2)
    image = ProcessedImageField(upload_to='static/event/',
                                 processors=[ResizeToFit(width=300, height=300)],
                                 format='JPEG',
                                 options={'quality': 90},null=True)
  

    def __str__(self):
        return f"{self.nom} {self.description}"

class Realisation(models.Model):
    nom = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    date_de_fin = models.DateField()
    domaine_intervention = models.CharField(max_length=100)
    budget = models.DecimalField(max_digits=10, decimal_places=2)
    fond_collecter = models.IntegerField(default=0)
    image = ProcessedImageField(upload_to='static/realisation/',
                                 processors=[ResizeToFit(width=300, height=300)],
                                 format='JPEG',
                                 options={'quality': 90},null=True)
  
    def __str__(self):
        return f"{self.nom} {self.description}"

class Donation(models.Model):
    nom_du_donateur = models.CharField(max_length=30)
    montant = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField()
    methode_de_paiement = models.CharField(max_length=50)
    anonym = models.BooleanField()

    def __str__(self):
        return f"{self.nom_du_donateur} {self.montant}"

class Partenaire(models.Model):
    nom = models.CharField(max_length=30)
    prenom = models.CharField(max_length=30)
    domaine = models.CharField(max_length=50)
    capacite = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.nom} {self.prenom}"
class Contact(models.Model):
    nom = models.CharField(max_length=30)
    email = models.EmailField(max_length=50)
    phone = models.CharField(max_length=15)
    message = models.CharField(max_length=255)
    
    def __str__(self):
        return f"{self.nom}"
class ProjetAvenir(models.Model):
    nom = models.CharField(max_length=100)
    description = models.CharField(max_length = 255)
    budget_souhaite= models.IntegerField(default=0)
    budget_actuelle= models.IntegerField(default=0)
    image = ProcessedImageField(upload_to='static/projet/',
                                 processors=[ResizeToFit(width=300, height=300)],
                                 format='JPEG',
                                 options={'quality': 90},null=True)
  
  
    def __str__(self):
        return self.nom
class Equipe(models.Model):
    nom = models.CharField(max_length=50)
    poste = models.CharField(max_length=50)
    profil = ProcessedImageField(upload_to='static/equipe/',
                                 processors=[ResizeToFit(width=300, height=300)],
                                 format='JPEG',
                                 options={'quality': 90},null=True)
  
    
    def __str__(self):
        return self.nom
    