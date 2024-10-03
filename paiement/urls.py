from . import views
from django.urls import path



app_name = 'Paiement'

urlpatterns = [
    path('detail',views.index,name="paiement_home"),
    path("donate/",views.donations,name="donation"),
    path("paypal/",views.paypal,name="paypal"),
    
    
]