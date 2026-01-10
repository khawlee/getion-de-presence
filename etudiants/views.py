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


def ajouter_etudiant(request):
    if 'user_id' not in request.session:
        return redirect('login')

    message = ''
    form = EtudiantForm()

    if request.method == 'POST':
        form = EtudiantForm(request.POST, request.FILES)

        # 1️⃣ Validation Django
        if not form.is_valid():
            message = "Veuillez corriger les erreurs du formulaire."
            return render(request, 'etudiants/ajouter_etudiant.html', {
                'form': form,
                'message': message
            })

        # 2️⃣ Vérification explicite de la photo
        photo_file = form.cleaned_data.get('photo')
        if not photo_file:
            message = "Veuillez ajouter une photo."
            return render(request, 'etudiants/ajouter_etudiant.html', {
                'form': form,
                'message': message
            })

        # 3️⃣ Traitement visage
        try:
            image = face_recognition.load_image_file(photo_file)
            encodages = face_recognition.face_encodings(image)
        except Exception:
            message = "Photo invalide ou non lisible."
            return render(request, 'etudiants/ajouter_etudiant.html', {
                'form': form,
                'message': message
            })

        if not encodages:
            message = "Aucun visage détecté sur la photo."
            return render(request, 'etudiants/ajouter_etudiant.html', {
                'form': form,
                'message': message
            })

        encodage_nouveau = np.array(encodages[0])

        # 4️⃣ Détection de doublon
        for etu in Etudiant.objects.all():
            encodes_existant = np.array(eval(etu.encodage))
            distance = np.linalg.norm(encodes_existant - encodage_nouveau)
            if distance < 0.6:
                message = "Un étudiant avec ce visage existe déjà !"
                return render(request, 'etudiants/ajouter_etudiant.html', {
                    'form': form,
                    'message': message
                })

        # 5️⃣ Sauvegarde finale (SEULEMENT ICI)
        etu = form.save(commit=False)
        etu.encodage = encodage_nouveau.tolist()
        etu.save()

        message = "Étudiant ajouté avec succès !"
        return render(request, 'etudiants/ajouter_etudiant.html', {
            'form': EtudiantForm(),
            'message': message
        })

    return render(request, 'etudiants/ajouter_etudiant.html', {
        'form': form,
        'message': message
    })



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




