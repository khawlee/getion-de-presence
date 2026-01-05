from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_view, name='login'),
    path('admin_dashboard/', views.graphe, name='graphe'),
    path('ajouter/', views.ajouter_etudiant, name='ajouter_etudiant'),
]
