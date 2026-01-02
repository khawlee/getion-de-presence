from django.shortcuts import render, redirect
from .forms import EtudiantForm
from .models import Etudiant
import face_recognition
import numpy as np

def admin_page(request):
    return render(request, 'etudiants/admin_dashboard.html')

def ajouter_etudiant(request):
    message = ''
    if request.method == 'POST':
        form = EtudiantForm(request.POST, request.FILES)
        if form.is_valid():
            photo_file = request.FILES['photo']
            # Charger l'image
            image = face_recognition.load_image_file(photo_file)
            encodages = face_recognition.face_encodings(image)
            if not encodages:
                message = "Aucun visage détecté sur la photo."
            else:
                encodage_nouveau = encodages[0].tolist()  # convertir en liste pour TextField
                # Vérifier doublon
                doublon = False
                for etu in Etudiant.objects.all():
                    encodes_existant = np.array(eval(etu.encodage))
                    distance = np.linalg.norm(encodes_existant - encodage_nouveau)
                    if distance < 0.6:  # seuil typique de reconnaissance faciale
                        doublon = True
                        break
                if doublon:
                    message = "Un étudiant avec ce visage existe déjà !"
                else:
                    etu = form.save(commit=False)
                    etu.encodage = str(encodage_nouveau)
                    etu.save()
                    message = "Étudiant ajouté avec succès !"
                    form = EtudiantForm()  # reset form
    else:
        form = EtudiantForm()

    return render(request, 'etudiants/ajouter_etudiant.html', {'form': form, 'message': message})
