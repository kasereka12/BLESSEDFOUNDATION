from django.shortcuts import render , redirect
from django.http import HttpResponse
from .models import Ambassadeur , Adherant , Histoire , Contact , ProjetAvenir , Evenement , Realisation , Equipe
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings


# Home.
def index(request):
    histoires = Histoire.objects.filter(etat=True)
    projets = ProjetAvenir.objects.all()[:3]
    
    return render(request,'blessed_Foundation/index.html', {'histoires':histoires , 'projets': projets})

#Foundation Start
def about(request):
    return render(request,'blessed_Foundation/Foundation/about.html')

def Action(request):
    return render(request,'blessed_Foundation/Foundation/champAction.html')

def biograohie(request):
    return render(request,'blessed_Foundation/Foundation/biographie.html')
def Equipes(request):
    equipes = Equipe.objects.all()
    
    return render(request,'blessed_Foundation/Foundation/NotreEquipe.html', {'equipes' : equipes})
#Foundation End


#Impact Start
def Realisations(request):
    realisation =  Realisation.objects.all()
  
    return render(request,'blessed_Foundation/impact/realisation.html' , { 'realisations' : realisation})
def event(request):
    events = Evenement.objects.all()
    return render(request,'blessed_Foundation/impact/events.html' , { 'events' : events})

#Impact End

#join Start
def Adherer(request):
    if not request.user.is_authenticated:
        messages.error(request, "Vous devez être connecté pour accéder à cette page.")
        return redirect('login') 
    if request.method == "POST":
        typeperson = request.POST["type"]
        if typeperson == "individual" :
            nom = request.POST["nom"]
            postnom = request.POST["postnom"]
            prenom = request.POST["prenom"]
            sexe = request.POST["sexe"]
            lieudenaissance = request.POST["lieuNaissance"]
            datenaissance = request.POST["datenaissance"]
        address= request.POST["Address"]
        pays = request.POST["pays"]
        ville = request.POST["ville"]
        phone = request.POST["phone"]
        email = request.POST["email"]
        businessname= request.POST["businessname"]
        legalform = request.POST["legalform"]
        
        
        if typeperson == "individual" :
            new_Adherant = Adherant(
                nom=nom,
                post_nom=postnom,
                prenom=prenom,
                telephone=phone,
                genre=sexe,
                lieu_de_naissance=lieudenaissance,
                date_de_naissance=datenaissance,
                adresse=address,
                pays=pays,
                ville=ville,
                businessName="",
                legalForm="",    
            )
            new_Adherant.save()
            messages.success(request,"Vos données sont enregistrées vous serez contacter très rapidement")
        else :
            new_Adherant = Adherant(
                nom=businessname,
                post_nom="",
                prenom="",
                telephone=phone,
                genre="",
                lieu_de_naissance="",
                date_de_naissance='2000-01-01',
                adresse=address,
                pays=pays,
                ville=ville,
                businessName=businessname,
                legalForm=legalform,    
            )
            new_Adherant.save()
            messages.success(request,"Vos données sont enregistrées vous serez contacter très rapidement")
        
        admin_email = 'dmutaka7@gmail.com'  
        subject = 'Nouvelle demande d\'adhésion'
        message = f'Une nouvelle demande d\'adhésion a été soumise verifié votre panneau d\'administrateur pour plus de detail:\n\nTéléphone: {phone}\nEmail: {email}\nType: {typeperson}'
        
        send_mail(
            subject,
            message,
            settings.DEFAULT_FROM_EMAIL,
            [admin_email],
            fail_silently=False,
        )
            
        
    return render(request,'blessed_Foundation/join/Adherer.html')
def campagne(request):
    projets =  ProjetAvenir.objects.all()
    return render(request,'blessed_Foundation/join/campagne.html',{'projets': projets})
def Ambassadeurs(request):
    if not request.user.is_authenticated:
        messages.error(request, "Vous devez être connecté pour accéder à cette page.")
        return redirect('login')     
    if request.method == "POST":
        nom = request.POST["nom"]
        prenom = request.POST["prenom"]
        telephone = request.POST["phone"]
        pays = request.POST["pays"]
        ville = request.POST["ville"]
        profession = request.POST["profession"]
        email = request.POST["email"]
        raison = request.POST["raison"]
        profil = request.FILES["profil"]
        instagram = request.POST.get("instagram", "")
        facebook = request.POST.get("facebook", "")
        linkedin = request.POST.get("linkedin", "")
        youtube = request.POST.get("youtube", "")

        # Créer une nouvelle instance d'Ambassadeur avec les données reçues
        new_ambassadeur = Ambassadeur(
            nom=nom,
            prenom=prenom,
            telephone=telephone,
            pays=pays,
            ville=ville,
            profession=profession,
            email=email,
            raison=raison,
            profil=profil,
            instagram=instagram,
            facebook=facebook,
            linkedin=linkedin,
            youtube=youtube,
        )
        new_ambassadeur.save()
        admin_email = 'dmutaka7@gmail.com'  
        subject = 'Nouvelle demande d\'ambassadeur'
        message = f'Une nouvelle demande d\'ambassadeur a été soumise verifié votre panneau d\'administrateur pour plus de detail:\n\nTéléphone: {telephone}\nEmail: {email}\nNom: {nom}'
        
        send_mail(
            subject,
            message,
            settings.DEFAULT_FROM_EMAIL,
            [admin_email],
            fail_silently=False,
        )
        messages.success(request,"Vos données sont enregistrées vous serez contacter très rapidement")

       

    return render(request,'blessed_Foundation/join/DevenirAmbassadeur.html')
def Partenaire(request):
    return render(request,'blessed_Foundation/join/DevenirParteniare.html')
def Collecte(request):
    return render(request,'blessed_Foundation/join/LancerCollecte.html')
def Soutenir(request):
    return render(request,'blessed_Foundation/join/nousSoutenir.html')
def Histoires(request):
    if not request.user.is_authenticated:
        messages.error(request, "Vous devez être connecté pour accéder à cette page.")
        return redirect('login') 
    if request.method == "POST":
        nom = request.POST["nom"]
        prenom = request.POST["prenom"]
        telephone = request.POST["telephone"]
        mail = request.POST["mail"]
        stories = request.POST["histoire"]
        
        new_histoire = Histoire(
            nom = nom,
            prenom = prenom,
            email = mail,
            telephone = telephone,
            stories = stories
        )
        
        new_histoire.save()
        admin_email = 'dmutaka7@gmail.com'  
        subject = 'Nouvelle histoire enregistré'
        message = f'Une nouvelle story a été soumise verifié votre panneau d\'administrateur pour plus de detail:\n\nTéléphone: {telephone}\nEmail: {mail}\nNom: {nom}'
        
        send_mail(
            subject,
            message,
            settings.DEFAULT_FROM_EMAIL,
            [admin_email],
            fail_silently=False,
        )
        messages.success(request,"Merci d'avoir partagé votre histoire")
        

       
    return render(request,'blessed_Foundation/join/RaconteSonHistoire.html')



#Contact start
def contact(request):
    if request.method == "POST":
        nom = request.POST["nom"]
        email = request.POST["email"]
        telephone = request.POST["phone"]
        message = request.POST["Message"]
        
        new_contact = Contact(
            nom = nom,
            email = email,
            phone = telephone,
            message = message
        )
        new_contact.save()
        admin_email = 'dmutaka7@gmail.com'  
        subject = 'demande de contact site blessedFoundation'
        message = f'Un utilisateur desire vous contactez verifié votre panneau d\'administrateur pour plus de detail:\n\nTélephone: {phone}\nEmail: {email}\nNom: {nom}'
        
        send_mail(
            subject,
            message,
            settings.DEFAULT_FROM_EMAIL,
            [admin_email],
            fail_silently=False,
        )
        messages.success(request,"Merci de nous avoir contacté")
    return render(request,'blessed_Foundation/contact.html')
#Contact End
def error(request, *args, **kwargs):
    return render(request, 'blessed_Foundation/404.html') 