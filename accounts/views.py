from django.shortcuts import render , redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth import authenticate , login , logout
from django.contrib.auth.models import  User
from django.contrib.auth.hashers import make_password
from .models import PasswordResetToken
from django.utils.crypto import get_random_string
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages



#Connexion Start
def login_user(request):
    if request.method == 'POST':
        username = request.POST["username"]
        password = request.POST["password"]
        
        user = authenticate(request, username = username , password = password)
        if user is not None:
            login(request , user)
            return redirect('login')
        else:
            messages.info(request,"Identifiant ou mot de passe incorrect")
        
        
    if request.user.is_authenticated:
        return redirect('Foundation:index')
    return render(request,'blessed_Foundation/login.html')


def register_user(request):
    if request.method == 'POST':
        first_name = request.POST["first_name"]
        last_name = request.POST["last_name"]
        email = request.POST["email"]
        password = request.POST["password"]
        confirm_password = request.POST["confirm_password"]

        if password != confirm_password:
            messages.error(request, "Les mots de passe ne correspondent pas.")
            return redirect('register')
        user = User.objects.create_user(username=email, email=email, password=password,first_name=first_name, last_name=last_name)
        messages.success(request, "Inscription réussie. Vous pouvez vous connecter maintenant.")
        return redirect('Accounts:login')     
    return render(request, 'blessed_Foundation/register.html')


def recover_password(request):

    if request.method == 'POST':
        email = request.POST.get("email")
        try:
       
            user = User.objects.get(email=email)
            # Générer un jeton de réinitialisation
            token = get_random_string(length=32)
            PasswordResetToken.objects.create(user=user, token=token)
        
            # Envoyer un email avec le lien de réinitialisation
            reset_link = request.build_absolute_uri(f'change-password/{token}/')
            send_mail(
                'Réinitialisation de votre mot de passe',
                f'Cliquez sur le lien suivant pour réinitialiser votre mot de passe : {reset_link}',
                settings.DEFAULT_FROM_EMAIL,
                [email],
                fail_silently=False,
            )
            messages.success(request, "Un lien de réinitialisation a été envoyé à votre adresse email.")
            return redirect('login')
        except User.DoesNotExist:
            messages.error(request, "Aucun utilisateur trouvé avec cet email.")
    return render(request, 'blessed_Foundation/index_recover.html')

def change_password(request, token):
    reset_token = get_object_or_404(PasswordResetToken, token=token)
    if request.method == 'POST':
        password = request.POST.get("password")
        confirm_password = request.POST.get("Confirm_password")
        
        if password != confirm_password:
            messages.error(request, "Les mots de passe ne correspondent pas.")
            return render(request, 'blessed_Foundation/changePassword.html')

        user = reset_token.user
        user.password = make_password(password)
        user.save()
        reset_token.delete()  # Supprimer le jeton après utilisation
        messages.success(request, "Votre mot de passe a été mis à jour avec succès.")
        return redirect('login')
    
    return render(request, 'blessed_Foundation/changePassword.html')
def logout_user(request):
    logout(request)
    return redirect('Foundation:index')
    
#Connexion End
