from . import views
from django.urls import path



urlpatterns = [
    
    path("login/",views.login_user,name="login"),
    path("register/",views.register_user,name="register"),
    path("logout/",views.logout_user,name="logout"),
    path("recover",views.recover_password,name="recover"),
    path('change-password/<str:token>/', views.change_password, name='change_password'),
  
   
]