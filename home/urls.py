from django.urls import path
from . import views

urlpatterns = [
    path("", views.user_login, name="login"),  # Chemin pour la vue de connexion
    path("profile/", views.profile, name="profile"),  # Chemin pour la vue de profil
]
