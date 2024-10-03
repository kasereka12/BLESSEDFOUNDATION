from django.db import models
from django.utils import timezone


# Create your models here.
class MoyenDePaiement(models.Model):
    TYPE_PAIEMENT_CHOICES = [
        ('CARTE', 'Carte Bancaire'),
        ('ORANGE_MONEY', 'Orange Money'),
        ('M_PESA', 'M_pesa'),
        ('PAYPAL', 'PayPal'),
    ]

    id = models.AutoField(primary_key=True)
    nom = models.CharField(max_length=100)
    type_paiement = models.CharField(max_length=20, choices=TYPE_PAIEMENT_CHOICES)
    destinataire = models.CharField(max_length=255)
    details = models.JSONField(null=True, blank=True) 
    image = models.ImageField(upload_to='static/moyendePaiement/', null = True)
    date_ajout = models.DateTimeField(auto_now_add=True)
    date_modification = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.nom} - {self.get_type_paiement_display()}"
class Donateur(models.Model):
    code_transfert = models.CharField(max_length=50,null=True)
    nom_du_destinataire= models.CharField(max_length=50,null=True)
    nom = models.CharField(max_length=50, null=True)
    prenom = models.CharField(max_length=50 , null=True)
    telephone = models.CharField(max_length=20 , null=True )
    pays = models.CharField(max_length=50 , null=True)
    email = models.EmailField(null=True)
    message = models.TextField(null=True)
    decouverte = models.CharField(max_length = 50, null=True)
    date = models.DateTimeField(default=timezone.now())
    etat = models.BooleanField(default=False)
    def __str__(self):
        return f"{self.date}"
