from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_view, name='login'),
    path('dashboard/', views.graphe, name='dashboard'),
    path('ajouter_etudiant/', views.ajouter_etudiant, name='ajouter_etudiant'),
    path('gestion_utilisateurs/', views.gestion_utilisateurs, name='gestion_utilisateurs'),
    path('ajouter_utilisateur/', views.ajouter_utilisateur, name='ajouter_utilisateur'),
]
