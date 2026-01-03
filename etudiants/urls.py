from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_view, name='login'),
    path('admin_dashboard/', views.admin_page, name='admin_page'),
    path('ajouter/', views.ajouter_etudiant, name='ajouter_etudiant'),
]
