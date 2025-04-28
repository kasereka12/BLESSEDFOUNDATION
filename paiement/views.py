from django.shortcuts import render, get_object_or_404 , redirect
from .models import MoyenDePaiement, Donateur
from paypal.standard.forms import PayPalPaymentsForm
from django.conf import settings
import uuid
from django.urls import reverse
from django.core.serializers.json import DjangoJSONEncoder
import json
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# home.
def index(request):
    if request.method == 'POST':
        montant = request.POST.get('montant')
        types = request.POST.get('types')
        transfert = request.POST.get('transfert')
        destinataire = request.POST.get('destinataire')
        nom = request.POST.get('nom','')
        prenom = request.POST.get('prenom','')
        phone = request.POST.get('phone','')
        pays = request.POST.get('pays','')
        email = request.POST.get('email','')
        raison = request.POST.get('raison','')
        connaissance = request.POST.get('Connaissance','')
        donate =  Donateur(
            code_transfert=transfert,
            nom_du_destinataire=destinataire,
            nom=nom,
            prenom= prenom,
            telephone = phone,
            pays=pays, 
            email=email,
            message=raison,
            decouverte=connaissance
        )
       
        if type in ['M_PESA', 'ORANGE_MONEY']:
            donate.save()
            return redirect('Paiement:donation')
        else:
            donate_dict = {
            'code_transfert': donate.code_transfert,
            'nom_du_destinataire': donate.nom_du_destinataire,
            'nom': donate.nom,
            'montant':montant,
            'prenom': donate.prenom,
            'telephone': donate.telephone,
            'pays': donate.pays,
            'email': donate.email,
            'message': donate.message,
            'decouverte': donate.decouverte,
        }
        # Save the dictionary in the session
            request.session['donate'] = json.dumps(donate_dict, cls=DjangoJSONEncoder)
            return redirect('Paiement:paypal')
           
        
    mode = request.GET.get("mode")
    modes = get_object_or_404(MoyenDePaiement, id=mode)
    return render(request, "paiement/index.html", {'mode': modes})
def donations(request):
    mode = MoyenDePaiement.objects.all()
    return render(request,'paiement/donation.html', {'modes' : mode})


def paypal(request):
    if not request.user.is_authenticated:
        messages.error(request, "Vous devez être connecté pour accéder à cette page.")
        return redirect('login') 
    donate_data = json.loads(request.session.get('donate', '{}'))

    if not donate_data:
        return redirect('Paiement:paiement_home')  
    donate = Donateur(
        code_transfert=donate_data.get('code_transfert'),
        nom_du_destinataire=donate_data.get('nom_du_destinataire'),
        nom=donate_data.get('nom'),
        prenom=donate_data.get('prenom'),
        telephone=donate_data.get('telephone'),
        pays=donate_data.get('pays'),
        email=donate_data.get('email'),
        message=donate_data.get('message'),
        decouverte=donate_data.get('decouverte'),
       
    )
    donate.save()

    host = request.get_host()
    paypal_checkout = { 
        'business' : settings.PAYPAL_RECEIVED_EMAIL,
        'amount' : donate_data['montant'],
        'item_name' : 'essai',
        'invoice' : uuid.uuid4(),
        'currency_code' : 'USD',
        'notify_url': f"https://{host}{reverse('paypal-ipn')}",
        'return_url': f"http://{host}{reverse('Paiement:donation')}",
        'cancel_url': f"http://{host}{reverse('Paiement:paiement_home')}"
        
    }
    paypal_payment  = PayPalPaymentsForm(initial=paypal_checkout)
    return render(request,'paiement/checkout.html',{'paypal': paypal_payment ,'donate': donate})


#Donation End
