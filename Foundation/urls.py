"""
URL configuration for blessed_Foundation project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from . import views
from django.urls import path

app_name = 'Foundation'

urlpatterns = [
    path("",views.index,name="index"),
    path("about/",views.about,name="about"),
    path("event/",views.event,name="event"),
    path("Action/",views.Action,name="Action"),
    path("biographie/",views.biograohie,name="biographie"),
    path("equipe/",views.Equipes,name="equipe"),
    path("realisation/",views.Realisations,name="realisation"),
    path("adherer/",views.Adherer,name="adherer"),
    path("campagne/",views.campagne,name="campagne"),
    path("ambassadeur/",views.Ambassadeurs,name="ambassadeur"),
    path("partenaire/",views.Partenaire,name="partenaire"),
    path("collecte/",views.Collecte,name="collecte"),
    path("soutenir/",views.Soutenir,name="soutenir"),
    path("histoire/",views.Histoires,name="histoire"),
   
    path("contact/",views.contact,name="contact"),
    path("<path>/" ,views.error, name='error'),
   
]
