from django.shortcuts import render, redirect
from .models import Utilisateur, Etudiant
from .forms import EtudiantForm
import face_recognition
import numpy as np

# LOGIN
def login_view(request):
    message = ''
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        try:
            user = Utilisateur.objects.get(username=username, password=password)
            request.session['user_id'] = user.id
            request.session['role'] = user.role
            return redirect('dashboard')  # redirige vers graphe.html
        except Utilisateur.DoesNotExist:
            message = "Identifiants incorrects"
    return render(request, 'index.html', {'message': message})


# DASHBOARD
def graphe(request):
    if 'user_id' not in request.session:
        return redirect('login')
    return render(request, 'graphe.html')


# AJOUT ETUDIANT
def ajouter_etudiant(request):
    if 'user_id' not in request.session:
        return redirect('login')

    message = ''
    if request.method == 'POST':
        form = EtudiantForm(request.POST, request.FILES)
        if form.is_valid():
            photo_file = request.FILES['photo']
            image = face_recognition.load_image_file(photo_file)
            encodages = face_recognition.face_encodings(image)

            if not encodages:
                message = "Aucun visage détecté sur la photo."
            else:
                encodage_nouveau = encodages[0].tolist()
                doublon = False
                for etu in Etudiant.objects.all():
                    encodes_existant = np.array(eval(etu.encodage))
                    distance = np.linalg.norm(encodes_existant - encodage_nouveau)
                    if distance < 0.6:
                        doublon = True
                        break
                if doublon:
                    message = "Un étudiant avec ce visage existe déjà !"
                else:
                    etu = form.save(commit=False)
                    etu.encodage = str(encodage_nouveau)
                    etu.save()
                    message = "Étudiant ajouté avec succès !"
                    form = EtudiantForm()
    else:
        form = EtudiantForm()

    return render(request, 'etudiants/ajouter_etudiant.html', {'form': form, 'message': message})


# GESTION UTILISATEURS
def gestion_utilisateurs(request):
    if request.session.get('role') != 'SUPER_ADMIN':
        return redirect('dashboard')
    utilisateurs = Utilisateur.objects.exclude(role='SUPER_ADMIN')
    return render(request, 'etudiants/gestion_utilisateurs.html', {'utilisateurs': utilisateurs})


# AJOUT UTILISATEUR
def ajouter_utilisateur(request):
    if request.session.get('role') != 'SUPER_ADMIN':
        return redirect('dashboard')

    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        role = request.POST['role']

        Utilisateur.objects.create(username=username, email=email, password=password, role=role)
        return redirect('gestion_utilisateurs')

    return render(request, 'etudiants/ajouter_utilisateur.html')
