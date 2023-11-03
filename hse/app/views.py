from django.shortcuts import render ,redirect
from django.contrib.auth import authenticate , login ,logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .models import checklist_permis_feu_prest, document_jov

from .models import *

from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.models import User

from .forms import *

from app.somme import *
import matplotlib.dates as mdates

import matplotlib.pyplot as plt
from io import BytesIO
import base64
from app.models import UserProfile
import pandas as pd
# Create your views here.

# def performance(request):
#     donnees = Performance_sante.objects.all()
#     heure = [item.heure_travailler for item in donnees]
#     accident = [item.accident for item in donnees]
#     poste = [item.poste_adapte for item in donnees]
#     soins = [item.soins_medicaux for item in donnees]
#     secours = [item.premier_secours for item in donnees]
#     presque = [item.presque_accident for item in donnees]
    
#     context = {'heure':heure, 'accident':accident, 'poste':poste, 'soins':soins, 'secours':secours, 'presque':presque}
#     return render(request, 'KPI/KPI_jov.html', context)



def loginPage(request):
    
    # if request.user.is_authenticated:
    #     return redirect('home')
    
    # else :
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
            
        user=authenticate(request , username=username , password=password)
        
        if user is not None:
            login(request, user)
            try:
                id_poste = user.userprofile.id_poste  
                
                if id_poste.startswith('J'):
                    return redirect('KPI_jov')
                
                elif id_poste.startswith('P'):
                    return redirect('KPI_prest')
                
                elif id_poste.startswith('T'):
                    return redirect('KPI_trans')
                
                else:
                    return redirect('KPI_stat')
                
            except UserProfile.DoesNotExist:
                messages.info(request, "Username doesn't exist")
        else:
            messages.info(request, 'Username or password incorrect')
            
    return render(request, 'app/login.html')

def logoutUser(request):
    logout(request)
    return redirect('login')

# Accueil

def accueil_jov(request):
    context={}
    
    return render(request, 'accueil/accueil_jov.html')

def accueil_prest(request):
    context={}
    
    return render(request, 'accueil/accueil_prest.html')

def accueil_stat(request):
    context = {}
    
    return render(request, 'accueil/accueil_stat.html')

def accueil_trans(request):
    context = {}
    
    return render(request, 'accueil/accueil_trans.html')

# Base Documentaire

def BD_jov(request):
    jovena = document_jov.objects.all()
    context={'jovena':jovena}
    
    return render(request, 'BD/BD_jov.html',context)

def BD_prest(request):
    prestataire = document_prest.objects.all()
    context={'prestataire':prestataire}
    
    return render(request, 'BD/BD_prest.html',context)

def BD_stat(request):
    station = document_stat.objects.all()
    context = {'station':station}
    
    return render(request, 'BD/BD_stat.html', context)

def BD_trans(request):
    transporteur = document_trans.objects.all()
    context = {'transporteur':transporteur}
    
    return render(request, 'BD/BD_trans.html', context)


# Politique

def politique_jov(request):
    articles = document_jov.objects.all()
    context={'articles':articles}
    
    return render(request, 'politique/politique_jov.html',context)

def politique_prest(request):
    articles = document_prest.objects.all()
    context={'articles':articles}
    
    
    return render(request, 'politique/politique_prest.html',context)

def politique_stat(request):
    articles = document_stat.objects.all()
    context={'articles':articles}
    
    
    return render(request, 'politique/politique_stat.html',context)

def politique_trans(request):
    articles = document_trans.objects.all()
    context={'articles':articles}
    
    
    return render(request, 'politique/politique_trans.html',context)

# Registre des incidents

def incident_jov(request):
    context={}
    
    return render(request, 'incident/incident_jov.html')

def incident_prest(request):
    context={}
    
    return render(request, 'incident/incident_prest.html')

def incident_stat(request):
    context = {}
    
    return render(request, 'incident/incident_stat.html')

def incident_trans(request):
    context = {}
    
    return render(request, 'incident/incident_trans.html')

# Indicateurs

def indicateur_jov(request):
    data_points = KPI_jovena.objects.all()
    x_data = [mdates.date2num(point.date) for point in data_points]
    y_data1 = [point.taux_frequence_incident for point in data_points]
    y_data2 = [point.taux_gravite_incident for point in data_points]

    # Créez un DataFrame à partir des données
    data_df = pd.DataFrame({'date': x_data, 'taux_frequence': y_data1, 'taux_gravite': y_data2})

    # Triez le DataFrame par date
    data_df = data_df.sort_values(by='date')

    # Récupérez les données triées
    x_data_sorted = data_df['date']
    y_data1_sorted = data_df['taux_frequence']
    y_data2_sorted = data_df['taux_gravite']

    # Créez le premier graphique en utilisant les données triées
    fig, ax1 = plt.subplots(figsize=(6.5, 5))
    ax1.plot(x_data_sorted, y_data1_sorted, marker='o', linestyle='-')  # Utilisez plot à la place de scatter
    ax1.set_title('Taux de Fréquence d\'Incident')  # Mettez à jour le titre si nécessaire
    ax1.set_xlabel('Date')
    ax1.set_ylabel('Taux de Fréquence')
    ax1.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
    ax1.xaxis.set_major_locator(mdates.MonthLocator(interval=3))

    # Convertissez le premier graphique en une image
    buffer1 = BytesIO()
    plt.savefig(buffer1, format='png')
    buffer1.seek(0)
    image_png1 = buffer1.getvalue()
    buffer1.close()

    # Créez le deuxième graphique
    fig, ax2 = plt.subplots(figsize=(6.5, 5))
    ax2.plot(x_data_sorted, y_data2_sorted, marker='o', linestyle='-')
    ax2.set_title('Taux de Gravité d\'Incident')
    ax2.set_xlabel('Date')
    ax2.set_ylabel('Taux de Gravité')
    ax2.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m'))
    ax2.xaxis.set_major_locator(mdates.MonthLocator(interval=2))

    # Convertissez le deuxième graphique en une image
    buffer2 = BytesIO()
    plt.savefig(buffer2, format='png')
    buffer2.seek(0)
    image_png2 = buffer2.getvalue()
    buffer2.close()

    # Créez le troisième graphique en utilisant les données triées
    fig, ax3 = plt.subplots(figsize=(13.2, 7))
    ax3.plot(x_data_sorted, [a * b for a, b in zip(y_data2_sorted, y_data1_sorted)], marker='o', linestyle='-')  # Relier les points avec des lignes
    ax3.set_title('Taux de Fréquence x Taux de Gravité')
    ax3.set_xlabel('Date')
    ax3.set_ylabel('Résultat')
    ax3.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m'))
    ax3.xaxis.set_major_locator(mdates.MonthLocator(interval=1))

    buffer3 = BytesIO()
    plt.savefig(buffer3, format='png')
    buffer3.seek(0)
    image_png3 = buffer3.getvalue()
    buffer3.close()

    context = {
        'graphic1': base64.b64encode(image_png1).decode(),
        'graphic2': base64.b64encode(image_png2).decode(),
        'graphic3': base64.b64encode(image_png3).decode(),
    }

    return render(request, 'indicateur/indicateur_jov.html', context)
# def indicateur_jov(request):
    
#     data_points = KPI_jovena.objects.all()
#     x_data = [mdates.date2num(point.date) for point in data_points]
#     y_data = [point.taux_frequence_incident for point in data_points]
    
#     x_data2 = [mdates.date2num(point.date) for point in data_points]
#     y_data2 = [point.taux_gravite_incident for point in data_points]
    
#     # Créez un graphique Matplotlib
#     plt.figure(figsize=(8, 6))
#     plt.scatter(x_data, y_data)
#     plt.scatter(x_data2, y_data2)
#     plt.title('Scatter Plot of Data Points')
#     plt.xlabel('X-axis')
#     plt.ylabel('Y-axis')
    
#     # Formatage de l'axe des x pour afficher des dates
#     plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
#     plt.gca().xaxis.set_major_locator(mdates.DayLocator(interval=1))  # Afficher toutes les dates


#     # Convertissez le graphique en une image pour l'afficher dans le modèle de rendu
#     buffer = BytesIO()
#     plt.savefig(buffer, format='png')
#     buffer.seek(0)
#     image_png = buffer.getvalue()
#     buffer.close()

#     # Intégrez l'image dans une balise <img> de données base64
#     graphic = base64.b64encode(image_png).decode()
    
    
#     context={'graphic': graphic}
    
#     return render(request, 'indicateur/indicateur_jov.html', context)

def indicateur_prest(request):
    data_points = KPI_prestataire.objects.all()
    x_data = [mdates.date2num(point.date) for point in data_points]
    y_data1 = [point.taux_frequence_incident for point in data_points]
    y_data2 = [point.taux_gravite_incident for point in data_points]

    # Créez un DataFrame à partir des données
    data_df = pd.DataFrame({'date': x_data, 'taux_frequence': y_data1, 'taux_gravite': y_data2})

    # Triez le DataFrame par date
    data_df = data_df.sort_values(by='date')

    # Récupérez les données triées
    x_data_sorted = data_df['date']
    y_data1_sorted = data_df['taux_frequence']
    y_data2_sorted = data_df['taux_gravite']

    # Créez le premier graphique en utilisant les données triées
    fig, ax1 = plt.subplots(figsize=(6.5, 5))
    ax1.plot(x_data_sorted, y_data1_sorted, marker='o', linestyle='-')  # Utilisez plot à la place de scatter
    ax1.set_title('Taux de Fréquence d\'Incident')  # Mettez à jour le titre si nécessaire
    ax1.set_xlabel('Date')
    ax1.set_ylabel('Taux de Fréquence')
    ax1.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
    ax1.xaxis.set_major_locator(mdates.MonthLocator(interval=2))

    # Convertissez le premier graphique en une image
    buffer1 = BytesIO()
    plt.savefig(buffer1, format='png')
    buffer1.seek(0)
    image_png1 = buffer1.getvalue()
    buffer1.close()

    # Créez le deuxième graphique
    fig, ax2 = plt.subplots(figsize=(6.5, 5))
    ax2.plot(x_data_sorted, y_data2_sorted, marker='o', linestyle='-')
    ax2.set_title('Taux de Gravité d\'Incident')
    ax2.set_xlabel('Date')
    ax2.set_ylabel('Taux de Gravité')
    ax2.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m'))
    ax2.xaxis.set_major_locator(mdates.MonthLocator(interval=2))

    # Convertissez le deuxième graphique en une image
    buffer2 = BytesIO()
    plt.savefig(buffer2, format='png')
    buffer2.seek(0)
    image_png2 = buffer2.getvalue()
    buffer2.close()

    # Créez le troisième graphique en utilisant les données triées
    fig, ax3 = plt.subplots(figsize=(13.2, 7))
    ax3.plot(x_data_sorted, [a * b for a, b in zip(y_data2_sorted, y_data1_sorted)], marker='o', linestyle='-')  # Relier les points avec des lignes
    ax3.set_title('Taux de Fréquence x Taux de Gravité')
    ax3.set_xlabel('Date')
    ax3.set_ylabel('Résultat')
    ax3.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m'))
    ax3.xaxis.set_major_locator(mdates.MonthLocator(interval=1))

    buffer3 = BytesIO()
    plt.savefig(buffer3, format='png')
    buffer3.seek(0)
    image_png3 = buffer3.getvalue()
    buffer3.close()

    context = {
        'graphic1': base64.b64encode(image_png1).decode(),
        'graphic2': base64.b64encode(image_png2).decode(),
        'graphic3': base64.b64encode(image_png3).decode(),
    }
    
    return render(request, 'indicateur/indicateur_prest.html',context)

def indicateur_stat(request):
    data_points = KPI_station_service.objects.all()
    x_data = [mdates.date2num(point.date) for point in data_points]
    y_data1 = [point.taux_frequence_incident for point in data_points]
    y_data2 = [point.taux_gravite_incident for point in data_points]

    # Créez un DataFrame à partir des données
    data_df = pd.DataFrame({'date': x_data, 'taux_frequence': y_data1, 'taux_gravite': y_data2})

    # Triez le DataFrame par date
    data_df = data_df.sort_values(by='date')

    # Récupérez les données triées
    x_data_sorted = data_df['date']
    y_data1_sorted = data_df['taux_frequence']
    y_data2_sorted = data_df['taux_gravite']

    # Créez le premier graphique en utilisant les données triées
    fig, ax1 = plt.subplots(figsize=(6.5, 5))
    ax1.plot(x_data_sorted, y_data1_sorted, marker='o', linestyle='-')  # Utilisez plot à la place de scatter
    ax1.set_title('Fréquence d\'Incident')  # Mettez à jour le titre si nécessaire
    ax1.set_xlabel('Date')
    ax1.set_ylabel('Taux de Fréquence')
    ax1.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
    ax1.xaxis.set_major_locator(mdates.MonthLocator(interval=2))

    # Convertissez le premier graphique en une image
    buffer1 = BytesIO()
    plt.savefig(buffer1, format='png')
    buffer1.seek(0)
    image_png1 = buffer1.getvalue()
    buffer1.close()

    # Créez le deuxième graphique
    fig, ax2 = plt.subplots(figsize=(6.5, 5))
    ax2.plot(x_data_sorted, y_data2_sorted, marker='o', linestyle='-')
    ax2.set_title('Taux de Gravité d\'Incident')
    ax2.set_xlabel('Date')
    ax2.set_ylabel('Taux de Gravité')
    ax2.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m'))
    ax2.xaxis.set_major_locator(mdates.MonthLocator(interval=2))

    # Convertissez le deuxième graphique en une image
    buffer2 = BytesIO()
    plt.savefig(buffer2, format='png')
    buffer2.seek(0)
    image_png2 = buffer2.getvalue()
    buffer2.close()

    # Créez le troisième graphique en utilisant les données triées
    fig, ax3 = plt.subplots(figsize=(13.2, 7))
    ax3.plot(x_data_sorted, [a * b for a, b in zip(y_data2_sorted, y_data1_sorted)], marker='o', linestyle='-')  # Relier les points avec des lignes
    ax3.set_title('Taux de Fréquence x Taux de Gravité')
    ax3.set_xlabel('Date')
    ax3.set_ylabel('Résultat')
    ax3.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m'))
    ax3.xaxis.set_major_locator(mdates.MonthLocator(interval=1))

    buffer3 = BytesIO()
    plt.savefig(buffer3, format='png')
    buffer3.seek(0)
    image_png3 = buffer3.getvalue()
    buffer3.close()

    context = {
        'graphic1': base64.b64encode(image_png1).decode(),
        'graphic2': base64.b64encode(image_png2).decode(),
        'graphic3': base64.b64encode(image_png3).decode(),
    }
    
    return render(request, 'indicateur/indicateur_stat.html',context)

def indicateur_trans(request):
    data_points = KPI_transporteur.objects.all()
    x_data = [mdates.date2num(point.date) for point in data_points]
    y_data1 = [point.taux_frequence_incident for point in data_points]
    y_data2 = [point.taux_gravite_incident for point in data_points]

    # Créez un DataFrame à partir des données
    data_df = pd.DataFrame({'date': x_data, 'taux_frequence': y_data1, 'taux_gravite': y_data2})

    # Triez le DataFrame par date
    data_df = data_df.sort_values(by='date')

    # Récupérez les données triées
    x_data_sorted = data_df['date']
    y_data1_sorted = data_df['taux_frequence']
    y_data2_sorted = data_df['taux_gravite']

    # Créez le premier graphique en utilisant les données triées
    fig, ax1 = plt.subplots(figsize=(6.5, 5))
    ax1.plot(x_data_sorted, y_data1_sorted, marker='o', linestyle='-')  # Utilisez plot à la place de scatter
    ax1.set_title('Taux de Fréquence d\'Incident')  # Mettez à jour le titre si nécessaire
    ax1.set_xlabel('Date')
    ax1.set_ylabel('Taux de Fréquence')
    ax1.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
    ax1.xaxis.set_major_locator(mdates.MonthLocator(interval=2))

    # Convertissez le premier graphique en une image
    buffer1 = BytesIO()
    plt.savefig(buffer1, format='png')
    buffer1.seek(0)
    image_png1 = buffer1.getvalue()
    buffer1.close()

    # Créez le deuxième graphique
    fig, ax2 = plt.subplots(figsize=(6.5, 5))
    ax2.plot(x_data_sorted, y_data2_sorted, marker='o', linestyle='-')
    ax2.set_title('Taux de Gravité d\'Incident')
    ax2.set_xlabel('Date')
    ax2.set_ylabel('Taux de Gravité')
    ax2.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m'))
    ax2.xaxis.set_major_locator(mdates.MonthLocator(interval=2))

    # Convertissez le deuxième graphique en une image
    buffer2 = BytesIO()
    plt.savefig(buffer2, format='png')
    buffer2.seek(0)
    image_png2 = buffer2.getvalue()
    buffer2.close()

    # Créez le troisième graphique en utilisant les données triées
    fig, ax3 = plt.subplots(figsize=(13.2, 7))
    ax3.plot(x_data_sorted, [a * b for a, b in zip(y_data2_sorted, y_data1_sorted)], marker='o', linestyle='-')  # Relier les points avec des lignes
    ax3.set_title('Taux de Fréquence x Taux de Gravité')
    ax3.set_xlabel('Date')
    ax3.set_ylabel('Résultat')
    ax3.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m'))
    ax3.xaxis.set_major_locator(mdates.MonthLocator(interval=1))

    buffer3 = BytesIO()
    plt.savefig(buffer3, format='png')
    buffer3.seek(0)
    image_png3 = buffer3.getvalue()
    buffer3.close()

    context = {
        'graphic1': base64.b64encode(image_png1).decode(),
        'graphic2': base64.b64encode(image_png2).decode(),
        'graphic3': base64.b64encode(image_png3).decode(),
    }
    
    return render(request, 'indicateur/indicateur_trans.html',context)

# Equipement

def equip_jov(request):
    context={}
    
    return render(request, 'equipement/equip_jov.html')

def equip_prest(request):
    context={}
    
    return render(request, 'equipement/equip_prest.html')

def equip_stat(request):
    context = {}
    
    return render(request, 'equipement/equip_stat.html')

def equip_trans(request):
    context = {}
    
    return render(request, 'equipement/equip_trans.html')

# Base de Donnée (informations)

def info_jov(request):
    user = request.user
    
    profil_utilisateur = UserProfile.objects.filter(user=user).first()
    
    context = {
        'user': user,
        'profil_utilisateur': profil_utilisateur,
    }
    
    return render(request, 'information/info_jov.html', context)

def info_prest(request):
    user = request.user
    
    profil_utilisateur = UserProfile.objects.filter(user=user).first()
    
    context = {
        'user': user,
        'profil_utilisateur': profil_utilisateur,
    }
    
    return render(request, 'information/info_prest.html', context)

def info_stat(request):
    user = request.user
    
    profil_utilisateur = UserProfile.objects.filter(user=user).first()
    
    context = {
        'user': user,
        'profil_utilisateur': profil_utilisateur,
    }
    
    return render(request, 'information/info_stat.html', context)

def info_trans(request):
    user = request.user
    
    profil_utilisateur = UserProfile.objects.filter(user=user).first()
    
    context = {
        'user': user,
        'profil_utilisateur': profil_utilisateur,
    }
    
    return render(request, 'information/info_trans.html', context)

# Checklist

def checklist_jov(request):
   
    context={}
    
    return render(request, 'checklist/checklist_jov.html',context)


# CheckList Permis de feu Prest
def checklist_prest(request):
    if request.method == 'POST':
        form_checklist_feu = checklist_permis_feu_prestForm(request.POST)
        
        if form_checklist_feu.is_valid():
            form_checklist_feu.save()            
            messages.info(request, 'reussi')
            return redirect('checklist_prest')
        else:
            messages.error(request, 'Tsy mety')
            print(messages.error)
            return redirect('checklist_prest')  
    else:
        form_checklist_feu = checklist_permis_feu_prestForm()
    
    context={'form_checklist_feu':form_checklist_feu}
    return render(request, 'checklist/checklist_prest.html',context)

# Checklist Permis d'excavation Prest
def checklist_excavation_prest(request):
    if request.method == 'POST':
        form_checklist_excavation = checklist_permis_excavation_prestForm(request.POST)
        
        if form_checklist_excavation.is_valid():
            form_checklist_excavation.save()
            messages.info(request, 'reussi')
            return redirect('checklist_permis_excavation_prest')
        else:
            messages.error(request, 'Tsy mety')
            print(messages.error)
            return redirect('checklist_permis_excavation_prest')
    else:
        form_checklist_excavation = checklist_permis_excavation_prestForm()
    
    context = {'form_checklist_excavation':form_checklist_excavation}
    return render(request, 'checklist/checklist_permis_excavation_prest.html', context)
            
# Checklist Espace Confine 
def checklist_espace_confine(request):
    if request.method == 'POST':
        form_checklist_espace_confine = checklist_espace_confineForm(request.POST)
        
        if form_checklist_espace_confine.is_valid():
            form_checklist_espace_confine.save()
            messages.info(request, 'reussi')
            return redirect('checklist_espace_confine_prest')
        else:
            messages.error(request, 'Tsy mety')
            print(messages.error)
            return redirect('checklist_espace_confine_prest')
    else:
        form_checklist_espace_confine = checklist_espace_confineForm()
        
    context = {'form_checklist_espace_confine':form_checklist_espace_confine}
    return render(request, 'checklist/checklist_espace_confine_prest.html', context)    
    
            


def checklist_stat(request):
    if request.method == 'POST':
        form_checklist = Checklist_statForm(request.POST)
        
        if form_checklist.is_valid():
            form_checklist.save()
            # Enregistrez les données du formulaire dans la base de données
            messages.info(request ,"reussi")
            return redirect('checklist_stat')  # Redirigez l'utilisateur vers une page de confirmation après l'enregistrement
        
    else:
       form_checklist = Checklist_statForm()
    
    context={'form_checklist':form_checklist}
   
    return render(request, 'checklist/checklist_stat.html', context)

def checklist_trans(request):
    
    context={}
    
    return render(request, 'checklist/checklist_trans.html',context)

def checklist_permis_excavation_prest(request):
    context = {}
    
    return render(request, 'checklist/checklist_permis_excavation_prest.html')

def checklist_espace_confine_prest(request):
    context = {}
    
    return render(request, 'checklist/checklist_espace_confine_prest.html')
    


# Parametre

def parametre_jov(request):
    
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            # Vous pouvez également vous connecter automatiquement l'utilisateur ici s'il est déconnecté.
            messages.success(request, 'Votre mot de passe a été modifié avec succès.')
            return redirect('parametre_jov')  
    else:
        form = PasswordChangeForm(request.user)
    context={'form':form}
    
    return render(request, 'parametre/parametre_jov.html',context)

def parametre_prest(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            # Vous pouvez également vous connecter automatiquement l'utilisateur ici s'il est déconnecté.
            messages.success(request, 'Votre mot de passe a été modifié avec succès.')
            return redirect('parametre_prest',context)  
    else:
        form = PasswordChangeForm(request.user)
    context={'form':form}
    
    return render(request, 'parametre/parametre_prest.html',context)

def parametre_stat(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            # Vous pouvez également vous connecter automatiquement l'utilisateur ici s'il est déconnecté.
            messages.success(request, 'Votre mot de passe a été modifié avec succès.')
            return redirect('parametre_stat')  
    else:
        form = PasswordChangeForm(request.user)
    context={'form':form}
    
    return render(request, 'parametre/parametre_stat.html',context)

def parametre_trans(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            # Vous pouvez également vous connecter automatiquement l'utilisateur ici s'il est déconnecté.
            messages.success(request, 'Votre mot de passe a été modifié avec succès.')
            return redirect('parametre_trans')  
    else:
        form = PasswordChangeForm(request.user)
    context={'form':form}
    
    return render(request, 'parametre/parametre_trans.html',context)



# KPI Jovena
def KPI_jov(request):
    # total_hommes = somme_hommes()
    somme_homme, somme_femme, somme_effectif_total_sur_site,somme_heure_travailler,somme_fatalite,somme_accident,somme_poste_adapte,somme_soins_medicaux,somme_premier_secours,somme_presque_accident,somme_dommage_materiel,somme_heure_perdue,somme_km_parcouru,somme_nombre_incident,somme_nombre_acceleration_brusque,somme_nombre_depassement,somme_nombre_freinage_brusque,somme_nombre_de_malades,somme_violation_des_regles,somme_nombre_de_deversement,somme_volume_de_deversement,somme_surface_impactee,somme_nombre_inspection,somme_zones_de_dechets,somme_zones_de_stockage,somme_dechets_inerte,somme_dechets_organique,somme_dechets_plastique,somme_dechets_hydrocarbure,somme_dechets_d3e,somme_eaux_usees,somme_consommation_eau_extraite,somme_consommation_de_carburant,somme_consommation_electricite,somme_valeur_limite_seuil,somme_x_sur_site,somme_x_aux_racepteurs,somme_x_source_emission,somme_x_qualite_de_air,somme_x_sante,somme_x_securite,somme_x_environnement,somme_x_social,somme_aucun_incident_social,somme_nombre_de_travailleurs_migrants,somme_nombre_de_travailleurs_locaux,somme_pourcentage_main_oeuvre,somme_duree_moyenne_travail,somme_logement_des_travailleurs,somme_approvionnement_eau_potable,somme_nombre_acticivite_engagement,somme_nombre_activites,somme_induction_sur_site,somme_exercice_urgence,somme_toolbox,somme_formation_specifique,somme_starter,somme_nombre_outil_hsses,somme_nombre_inspection_hsses, somme_totale = somme_jovena()
    ttl1=somme_totale
    ttl=(somme_totale * 1000000)/somme_effectif_total_sur_site

    if request.method == 'POST':
        start_date = request.POST['start_date']
        end_date = request.POST['end_date']
        events = KPI_jovena.objects.filter(date__range=[start_date, end_date])
        return render(request, 'KPI/KPI_jov.html', {'events':events,
                                                    'somme_homme': somme_homme,
                                                    'somme_femme': somme_femme,
                                                    'somme_effectif_total_sur_site': somme_effectif_total_sur_site,
                                                    'somme_heure_travailler':somme_heure_travailler,
                                                    'somme_fatalite':somme_fatalite,
                                                    'somme_accident':somme_accident,
                                                    'somme_poste_adapte':somme_poste_adapte,
                                                    'somme_soins_medicaux':somme_soins_medicaux,
                                                    'somme_premier_secours':somme_premier_secours,
                                                    'somme_presque_accident':somme_presque_accident,
                                                    'somme_dommage_materiel':somme_dommage_materiel,
                                                    'somme_heure_perdue':somme_heure_perdue,
                                                    'somme_km_parcouru':somme_km_parcouru,
                                                    'somme_km_parcouru':somme_km_parcouru,
                                                    'somme_nombre_incident':somme_nombre_incident,
                                                    'somme_nombre_acceleration_brusque':somme_nombre_acceleration_brusque,
                                                    'somme_nombre_freinage_brusque':somme_nombre_freinage_brusque,
                                                    'somme_nombre_depassement':somme_nombre_depassement,
                                                    
                                                    'somme_nombre_de_malades': somme_nombre_de_malades,
                                                    'somme_violation_des_regles': somme_violation_des_regles,
                                                    'somme_nombre_de_deversement': somme_nombre_de_deversement,
                                                    'somme_volume_de_deversement': somme_volume_de_deversement,
                                                    'somme_surface_impactee': somme_surface_impactee,
                                                    'somme_nombre_inspection': somme_nombre_inspection,
                                                    'somme_zones_de_dechets': somme_zones_de_dechets,
                                                    'somme_zones_de_stockage': somme_zones_de_stockage,
                                                    'somme_dechets_inerte': somme_dechets_inerte,
                                                    'somme_dechets_organique': somme_dechets_organique,
                                                    'somme_dechets_plastique': somme_dechets_plastique,
                                                    'somme_dechets_hydrocarbure': somme_dechets_hydrocarbure,
                                                    'somme_dechets_d3e': somme_dechets_d3e,
                                                    'somme_eaux_usees': somme_eaux_usees,
                                                    'somme_consommation_eau_extraite': somme_consommation_eau_extraite,
                                                    'somme_consommation_de_carburant': somme_consommation_de_carburant,
                                                    'somme_consommation_electricite': somme_consommation_electricite,
                                                    'somme_valeur_limite_seuil': somme_valeur_limite_seuil,
                                                    'somme_x_sur_site': somme_x_sur_site,
                                                    'somme_x_aux_racepteurs': somme_x_aux_racepteurs,
                                                    'somme_x_source_emission': somme_x_source_emission,
                                                    'somme_x_qualite_de_air': somme_x_qualite_de_air,
                                                    'somme_x_sante': somme_x_sante,
                                                    'somme_x_securite': somme_x_securite,
                                                    'somme_x_environnement': somme_x_environnement,
                                                    'somme_x_social': somme_x_social,
                                                    'somme_aucun_incident_social': somme_aucun_incident_social,
                                                    'somme_nombre_de_travailleurs_migrants': somme_nombre_de_travailleurs_migrants,
                                                    'somme_nombre_de_travailleurs_locaux': somme_nombre_de_travailleurs_locaux,
                                                    'somme_pourcentage_main_oeuvre': somme_pourcentage_main_oeuvre,
                                                    'somme_duree_moyenne_travail': somme_duree_moyenne_travail,
                                                    'somme_logement_des_travailleurs': somme_logement_des_travailleurs,
                                                    'somme_approvionnement_eau_potable': somme_approvionnement_eau_potable,
                                                    'somme_nombre_acticivite_engagement': somme_nombre_acticivite_engagement,
                                                    'somme_nombre_activites': somme_nombre_activites,
                                                    'somme_induction_sur_site': somme_induction_sur_site,
                                                    'somme_exercice_urgence': somme_exercice_urgence,
                                                    'somme_toolbox': somme_toolbox,
                                                    'somme_formation_specifique': somme_formation_specifique,
                                                    'somme_starter': somme_starter,
                                                    'somme_nombre_outil_hsses': somme_nombre_outil_hsses,
                                                    'somme_nombre_inspection_hsses': somme_nombre_inspection_hsses,
                                                    'ttl':ttl,
                                                    'ttl1':ttl1
                                                    })
    else:
        events = KPI_jovena.objects.all()
        ttl1=somme_totale
        ttl=(somme_totale * 1000000)/somme_effectif_total_sur_site

    context = { 'events':events,
                'somme_homme': somme_homme,
                'somme_femme': somme_femme,
                'somme_effectif_total_sur_site': somme_effectif_total_sur_site,
                'somme_heure_travailler':somme_heure_travailler,
                'somme_fatalite':somme_fatalite,
                'somme_accident':somme_accident,
                'somme_poste_adapte':somme_poste_adapte,
                'somme_soins_medicaux':somme_soins_medicaux,
                'somme_premier_secours':somme_premier_secours,
                'somme_presque_accident':somme_presque_accident,
                'somme_dommage_materiel':somme_dommage_materiel,
                'somme_heure_perdue':somme_heure_perdue,
                'somme_km_parcouru':somme_km_parcouru,
                'somme_km_parcouru':somme_km_parcouru,
                'somme_nombre_incident':somme_nombre_incident,
                'somme_nombre_acceleration_brusque':somme_nombre_acceleration_brusque,
                'somme_nombre_freinage_brusque':somme_nombre_freinage_brusque,
                'somme_nombre_depassement':somme_nombre_depassement,
                
                'somme_nombre_de_malades': somme_nombre_de_malades,
                'somme_violation_des_regles': somme_violation_des_regles,
                'somme_nombre_de_deversement': somme_nombre_de_deversement,
                'somme_volume_de_deversement': somme_volume_de_deversement,
                'somme_surface_impactee': somme_surface_impactee,
                'somme_nombre_inspection': somme_nombre_inspection,
                'somme_zones_de_dechets': somme_zones_de_dechets,
                'somme_zones_de_stockage': somme_zones_de_stockage,
                'somme_dechets_inerte': somme_dechets_inerte,
                'somme_dechets_organique': somme_dechets_organique,
                'somme_dechets_plastique': somme_dechets_plastique,
                'somme_dechets_hydrocarbure': somme_dechets_hydrocarbure,
                'somme_dechets_d3e': somme_dechets_d3e,
                'somme_eaux_usees': somme_eaux_usees,
                'somme_consommation_eau_extraite': somme_consommation_eau_extraite,
                'somme_consommation_de_carburant': somme_consommation_de_carburant,
                'somme_consommation_electricite': somme_consommation_electricite,
                'somme_valeur_limite_seuil': somme_valeur_limite_seuil,
                'somme_x_sur_site': somme_x_sur_site,
                'somme_x_aux_racepteurs': somme_x_aux_racepteurs,
                'somme_x_source_emission': somme_x_source_emission,
                'somme_x_qualite_de_air': somme_x_qualite_de_air,
                'somme_x_sante': somme_x_sante,
                'somme_x_securite': somme_x_securite,
                'somme_x_environnement': somme_x_environnement,
                'somme_x_social': somme_x_social,
                'somme_aucun_incident_social': somme_aucun_incident_social,
                'somme_nombre_de_travailleurs_migrants': somme_nombre_de_travailleurs_migrants,
                'somme_nombre_de_travailleurs_locaux': somme_nombre_de_travailleurs_locaux,
                'somme_pourcentage_main_oeuvre': somme_pourcentage_main_oeuvre,
                'somme_duree_moyenne_travail': somme_duree_moyenne_travail,
                'somme_logement_des_travailleurs': somme_logement_des_travailleurs,
                'somme_approvionnement_eau_potable': somme_approvionnement_eau_potable,
                'somme_nombre_acticivite_engagement': somme_nombre_acticivite_engagement,
                'somme_nombre_activites': somme_nombre_activites,
                'somme_induction_sur_site': somme_induction_sur_site,
                'somme_exercice_urgence': somme_exercice_urgence,
                'somme_toolbox': somme_toolbox,
                'somme_formation_specifique': somme_formation_specifique,
                'somme_starter': somme_starter,
                'somme_nombre_outil_hsses': somme_nombre_outil_hsses,
                'somme_nombre_inspection_hsses': somme_nombre_inspection_hsses,
                'ttl':ttl,
                'ttl1':ttl1
                }
    
    return render(request, 'KPI/KPI_jov.html', context)

def KPI_prest(request):
    somme_homme, somme_femme, somme_effectif_total_sur_site,somme_heure_travailler,somme_fatalite,somme_accident,somme_poste_adapte,somme_soins_medicaux,somme_premier_secours,somme_presque_accident,somme_dommage_materiel,somme_heure_perdue,somme_km_parcouru,somme_nombre_incident,somme_nombre_acceleration_brusque,somme_nombre_depassement,somme_nombre_freinage_brusque,somme_nombre_de_malades,somme_violation_des_regles,somme_nombre_de_deversement,somme_volume_de_deversement,somme_surface_impactee,somme_nombre_inspection,somme_zones_de_dechets,somme_zones_de_stockage,somme_dechets_inerte,somme_dechets_organique,somme_dechets_plastique,somme_dechets_hydrocarbure,somme_dechets_d3e,somme_eaux_usees,somme_consommation_eau_extraite,somme_consommation_de_carburant,somme_consommation_electricite,somme_valeur_limite_seuil,somme_x_sur_site,somme_x_aux_racepteurs,somme_x_source_emission,somme_x_qualite_de_air,somme_x_sante,somme_x_securite,somme_x_environnement,somme_x_social,somme_aucun_incident_social,somme_nombre_de_travailleurs_migrants,somme_nombre_de_travailleurs_locaux,somme_pourcentage_main_oeuvre,somme_duree_moyenne_travail,somme_logement_des_travailleurs,somme_approvionnement_eau_potable,somme_nombre_acticivite_engagement,somme_nombre_activites,somme_induction_sur_site,somme_exercice_urgence,somme_toolbox,somme_formation_specifique,somme_starter,somme_nombre_outil_hsses,somme_nombre_inspection_hsses, somme_totale = somme_prestataire()
    ttl1=somme_totale
    ttl=(somme_totale * 1000000)/somme_effectif_total_sur_site
    
    if request.method == 'POST':
        start_date = request.POST['start_date']
        end_date = request.POST['end_date']
        events = KPI_prestataire.objects.filter(date__range=[start_date, end_date])
        return render(request, 'KPI/KPI_prest.html', {'events':events,
                                                    'somme_homme': somme_homme,
                                                    'somme_femme': somme_femme,
                                                    'somme_effectif_total_sur_site': somme_effectif_total_sur_site,
                                                    'somme_heure_travailler':somme_heure_travailler,
                                                    'somme_fatalite':somme_fatalite,
                                                    'somme_accident':somme_accident,
                                                    'somme_poste_adapte':somme_poste_adapte,
                                                    'somme_soins_medicaux':somme_soins_medicaux,
                                                    'somme_premier_secours':somme_premier_secours,
                                                    'somme_presque_accident':somme_presque_accident,
                                                    'somme_dommage_materiel':somme_dommage_materiel,
                                                    'somme_heure_perdue':somme_heure_perdue,
                                                    'somme_km_parcouru':somme_km_parcouru,
                                                    'somme_km_parcouru':somme_km_parcouru,
                                                    'somme_nombre_incident':somme_nombre_incident,
                                                    'somme_nombre_acceleration_brusque':somme_nombre_acceleration_brusque,
                                                    'somme_nombre_freinage_brusque':somme_nombre_freinage_brusque,
                                                    'somme_nombre_depassement':somme_nombre_depassement,
                                                    
                                                    'somme_nombre_de_malades': somme_nombre_de_malades,
                                                    'somme_violation_des_regles': somme_violation_des_regles,
                                                    'somme_nombre_de_deversement': somme_nombre_de_deversement,
                                                    'somme_volume_de_deversement': somme_volume_de_deversement,
                                                    'somme_surface_impactee': somme_surface_impactee,
                                                    'somme_nombre_inspection': somme_nombre_inspection,
                                                    'somme_zones_de_dechets': somme_zones_de_dechets,
                                                    'somme_zones_de_stockage': somme_zones_de_stockage,
                                                    'somme_dechets_inerte': somme_dechets_inerte,
                                                    'somme_dechets_organique': somme_dechets_organique,
                                                    'somme_dechets_plastique': somme_dechets_plastique,
                                                    'somme_dechets_hydrocarbure': somme_dechets_hydrocarbure,
                                                    'somme_dechets_d3e': somme_dechets_d3e,
                                                    'somme_eaux_usees': somme_eaux_usees,
                                                    'somme_consommation_eau_extraite': somme_consommation_eau_extraite,
                                                    'somme_consommation_de_carburant': somme_consommation_de_carburant,
                                                    'somme_consommation_electricite': somme_consommation_electricite,
                                                    'somme_valeur_limite_seuil': somme_valeur_limite_seuil,
                                                    'somme_x_sur_site': somme_x_sur_site,
                                                    'somme_x_aux_racepteurs': somme_x_aux_racepteurs,
                                                    'somme_x_source_emission': somme_x_source_emission,
                                                    'somme_x_qualite_de_air': somme_x_qualite_de_air,
                                                    'somme_x_sante': somme_x_sante,
                                                    'somme_x_securite': somme_x_securite,
                                                    'somme_x_environnement': somme_x_environnement,
                                                    'somme_x_social': somme_x_social,
                                                    'somme_aucun_incident_social': somme_aucun_incident_social,
                                                    'somme_nombre_de_travailleurs_migrants': somme_nombre_de_travailleurs_migrants,
                                                    'somme_nombre_de_travailleurs_locaux': somme_nombre_de_travailleurs_locaux,
                                                    'somme_pourcentage_main_oeuvre': somme_pourcentage_main_oeuvre,
                                                    'somme_duree_moyenne_travail': somme_duree_moyenne_travail,
                                                    'somme_logement_des_travailleurs': somme_logement_des_travailleurs,
                                                    'somme_approvionnement_eau_potable': somme_approvionnement_eau_potable,
                                                    'somme_nombre_acticivite_engagement': somme_nombre_acticivite_engagement,
                                                    'somme_nombre_activites': somme_nombre_activites,
                                                    'somme_induction_sur_site': somme_induction_sur_site,
                                                    'somme_exercice_urgence': somme_exercice_urgence,
                                                    'somme_toolbox': somme_toolbox,
                                                    'somme_formation_specifique': somme_formation_specifique,
                                                    'somme_starter': somme_starter,
                                                    'somme_nombre_outil_hsses': somme_nombre_outil_hsses,
                                                    'somme_nombre_inspection_hsses': somme_nombre_inspection_hsses,
                                                    'ttl':ttl,
                                                    'ttl1':ttl1
                                                    })
    else:
        events = KPI_prestataire.objects.all()
        ttl1=somme_totale
        ttl=(somme_totale * 1000000)/somme_effectif_total_sur_site


    context = { 'events':events,
                'somme_homme': somme_homme,
                'somme_femme': somme_femme,
                'somme_effectif_total_sur_site': somme_effectif_total_sur_site,
                'somme_heure_travailler':somme_heure_travailler,
                'somme_fatalite':somme_fatalite,
                'somme_accident':somme_accident,
                'somme_poste_adapte':somme_poste_adapte,
                'somme_soins_medicaux':somme_soins_medicaux,
                'somme_premier_secours':somme_premier_secours,
                'somme_presque_accident':somme_presque_accident,
                'somme_dommage_materiel':somme_dommage_materiel,
                'somme_heure_perdue':somme_heure_perdue,
                'somme_km_parcouru':somme_km_parcouru,
                'somme_km_parcouru':somme_km_parcouru,
                'somme_nombre_incident':somme_nombre_incident,
                'somme_nombre_acceleration_brusque':somme_nombre_acceleration_brusque,
                'somme_nombre_freinage_brusque':somme_nombre_freinage_brusque,
                'somme_nombre_depassement':somme_nombre_depassement,
                
                'somme_nombre_de_malades': somme_nombre_de_malades,
                'somme_violation_des_regles': somme_violation_des_regles,
                'somme_nombre_de_deversement': somme_nombre_de_deversement,
                'somme_volume_de_deversement': somme_volume_de_deversement,
                'somme_surface_impactee': somme_surface_impactee,
                'somme_nombre_inspection': somme_nombre_inspection,
                'somme_zones_de_dechets': somme_zones_de_dechets,
                'somme_zones_de_stockage': somme_zones_de_stockage,
                'somme_dechets_inerte': somme_dechets_inerte,
                'somme_dechets_organique': somme_dechets_organique,
                'somme_dechets_plastique': somme_dechets_plastique,
                'somme_dechets_hydrocarbure': somme_dechets_hydrocarbure,
                'somme_dechets_d3e': somme_dechets_d3e,
                'somme_eaux_usees': somme_eaux_usees,
                'somme_consommation_eau_extraite': somme_consommation_eau_extraite,
                'somme_consommation_de_carburant': somme_consommation_de_carburant,
                'somme_consommation_electricite': somme_consommation_electricite,
                'somme_valeur_limite_seuil': somme_valeur_limite_seuil,
                'somme_x_sur_site': somme_x_sur_site,
                'somme_x_aux_racepteurs': somme_x_aux_racepteurs,
                'somme_x_source_emission': somme_x_source_emission,
                'somme_x_qualite_de_air': somme_x_qualite_de_air,
                'somme_x_sante': somme_x_sante,
                'somme_x_securite': somme_x_securite,
                'somme_x_environnement': somme_x_environnement,
                'somme_x_social': somme_x_social,
                'somme_aucun_incident_social': somme_aucun_incident_social,
                'somme_nombre_de_travailleurs_migrants': somme_nombre_de_travailleurs_migrants,
                'somme_nombre_de_travailleurs_locaux': somme_nombre_de_travailleurs_locaux,
                'somme_pourcentage_main_oeuvre': somme_pourcentage_main_oeuvre,
                'somme_duree_moyenne_travail': somme_duree_moyenne_travail,
                'somme_logement_des_travailleurs': somme_logement_des_travailleurs,
                'somme_approvionnement_eau_potable': somme_approvionnement_eau_potable,
                'somme_nombre_acticivite_engagement': somme_nombre_acticivite_engagement,
                'somme_nombre_activites': somme_nombre_activites,
                'somme_induction_sur_site': somme_induction_sur_site,
                'somme_exercice_urgence': somme_exercice_urgence,
                'somme_toolbox': somme_toolbox,
                'somme_formation_specifique': somme_formation_specifique,
                'somme_starter': somme_starter,
                'somme_nombre_outil_hsses': somme_nombre_outil_hsses,
                'somme_nombre_inspection_hsses': somme_nombre_inspection_hsses,
                'ttl':ttl,
                'ttl1':ttl1
                }
    return render(request, 'KPI/KPI_prest.html', context)

def KPI_trans(request):
    somme_homme, somme_femme, somme_effectif_total_sur_site,somme_heure_travailler,somme_fatalite,somme_accident,somme_poste_adapte,somme_soins_medicaux,somme_premier_secours,somme_presque_accident,somme_dommage_materiel,somme_heure_perdue,somme_km_parcouru,somme_nombre_incident,somme_nombre_acceleration_brusque,somme_nombre_depassement,somme_nombre_freinage_brusque,somme_nombre_de_malades,somme_violation_des_regles,somme_nombre_de_deversement,somme_volume_de_deversement,somme_surface_impactee,somme_nombre_inspection,somme_zones_de_dechets,somme_zones_de_stockage,somme_dechets_inerte,somme_dechets_organique,somme_dechets_plastique,somme_dechets_hydrocarbure,somme_dechets_d3e,somme_eaux_usees,somme_consommation_eau_extraite,somme_consommation_de_carburant,somme_consommation_electricite,somme_valeur_limite_seuil,somme_x_sur_site,somme_x_aux_racepteurs,somme_x_source_emission,somme_x_qualite_de_air,somme_x_sante,somme_x_securite,somme_x_environnement,somme_x_social,somme_aucun_incident_social,somme_nombre_de_travailleurs_migrants,somme_nombre_de_travailleurs_locaux,somme_pourcentage_main_oeuvre,somme_duree_moyenne_travail,somme_logement_des_travailleurs,somme_approvionnement_eau_potable,somme_nombre_acticivite_engagement,somme_nombre_activites,somme_induction_sur_site,somme_exercice_urgence,somme_toolbox,somme_formation_specifique,somme_starter,somme_nombre_outil_hsses,somme_nombre_inspection_hsses, somme_totale = somme_transporteur()
    ttl1=somme_totale
    ttl=(somme_totale * 1000000)/somme_effectif_total_sur_site
    
    if request.method == 'POST':
        start_date = request.POST['start_date']
        end_date = request.POST['end_date']
        events = KPI_transporteur.objects.filter(date__range=[start_date, end_date])
        return render(request, 'KPI/KPI_trans.html', {'events':events,
                                                    'somme_homme': somme_homme,
                                                    'somme_femme': somme_femme,
                                                    'somme_effectif_total_sur_site': somme_effectif_total_sur_site,
                                                    'somme_heure_travailler':somme_heure_travailler,
                                                    'somme_fatalite':somme_fatalite,
                                                    'somme_accident':somme_accident,
                                                    'somme_poste_adapte':somme_poste_adapte,
                                                    'somme_soins_medicaux':somme_soins_medicaux,
                                                    'somme_premier_secours':somme_premier_secours,
                                                    'somme_presque_accident':somme_presque_accident,
                                                    'somme_dommage_materiel':somme_dommage_materiel,
                                                    'somme_heure_perdue':somme_heure_perdue,
                                                    'somme_km_parcouru':somme_km_parcouru,
                                                    'somme_km_parcouru':somme_km_parcouru,
                                                    'somme_nombre_incident':somme_nombre_incident,
                                                    'somme_nombre_acceleration_brusque':somme_nombre_acceleration_brusque,
                                                    'somme_nombre_freinage_brusque':somme_nombre_freinage_brusque,
                                                    'somme_nombre_depassement':somme_nombre_depassement,
                                                    
                                                    'somme_nombre_de_malades': somme_nombre_de_malades,
                                                    'somme_violation_des_regles': somme_violation_des_regles,
                                                    'somme_nombre_de_deversement': somme_nombre_de_deversement,
                                                    'somme_volume_de_deversement': somme_volume_de_deversement,
                                                    'somme_surface_impactee': somme_surface_impactee,
                                                    'somme_nombre_inspection': somme_nombre_inspection,
                                                    'somme_zones_de_dechets': somme_zones_de_dechets,
                                                    'somme_zones_de_stockage': somme_zones_de_stockage,
                                                    'somme_dechets_inerte': somme_dechets_inerte,
                                                    'somme_dechets_organique': somme_dechets_organique,
                                                    'somme_dechets_plastique': somme_dechets_plastique,
                                                    'somme_dechets_hydrocarbure': somme_dechets_hydrocarbure,
                                                    'somme_dechets_d3e': somme_dechets_d3e,
                                                    'somme_eaux_usees': somme_eaux_usees,
                                                    'somme_consommation_eau_extraite': somme_consommation_eau_extraite,
                                                    'somme_consommation_de_carburant': somme_consommation_de_carburant,
                                                    'somme_consommation_electricite': somme_consommation_electricite,
                                                    'somme_valeur_limite_seuil': somme_valeur_limite_seuil,
                                                    'somme_x_sur_site': somme_x_sur_site,
                                                    'somme_x_aux_racepteurs': somme_x_aux_racepteurs,
                                                    'somme_x_source_emission': somme_x_source_emission,
                                                    'somme_x_qualite_de_air': somme_x_qualite_de_air,
                                                    'somme_x_sante': somme_x_sante,
                                                    'somme_x_securite': somme_x_securite,
                                                    'somme_x_environnement': somme_x_environnement,
                                                    'somme_x_social': somme_x_social,
                                                    'somme_aucun_incident_social': somme_aucun_incident_social,
                                                    'somme_nombre_de_travailleurs_migrants': somme_nombre_de_travailleurs_migrants,
                                                    'somme_nombre_de_travailleurs_locaux': somme_nombre_de_travailleurs_locaux,
                                                    'somme_pourcentage_main_oeuvre': somme_pourcentage_main_oeuvre,
                                                    'somme_duree_moyenne_travail': somme_duree_moyenne_travail,
                                                    'somme_logement_des_travailleurs': somme_logement_des_travailleurs,
                                                    'somme_approvionnement_eau_potable': somme_approvionnement_eau_potable,
                                                    'somme_nombre_acticivite_engagement': somme_nombre_acticivite_engagement,
                                                    'somme_nombre_activites': somme_nombre_activites,
                                                    'somme_induction_sur_site': somme_induction_sur_site,
                                                    'somme_exercice_urgence': somme_exercice_urgence,
                                                    'somme_toolbox': somme_toolbox,
                                                    'somme_formation_specifique': somme_formation_specifique,
                                                    'somme_starter': somme_starter,
                                                    'somme_nombre_outil_hsses': somme_nombre_outil_hsses,
                                                    'somme_nombre_inspection_hsses': somme_nombre_inspection_hsses,
                                                    'ttl':ttl,
                                                    'ttl1':ttl1
                                                    })
    else:
        events = KPI_transporteur.objects.all()
        ttl1=somme_totale
        ttl=(somme_totale * 1000000)/somme_effectif_total_sur_site

    context = { 'events':events,
                'somme_homme': somme_homme,
                'somme_femme': somme_femme,
                'somme_effectif_total_sur_site': somme_effectif_total_sur_site,
                'somme_heure_travailler':somme_heure_travailler,
                'somme_fatalite':somme_fatalite,
                'somme_accident':somme_accident,
                'somme_poste_adapte':somme_poste_adapte,
                'somme_soins_medicaux':somme_soins_medicaux,
                'somme_premier_secours':somme_premier_secours,
                'somme_presque_accident':somme_presque_accident,
                'somme_dommage_materiel':somme_dommage_materiel,
                'somme_heure_perdue':somme_heure_perdue,
                'somme_km_parcouru':somme_km_parcouru,
                'somme_km_parcouru':somme_km_parcouru,
                'somme_nombre_incident':somme_nombre_incident,
                'somme_nombre_acceleration_brusque':somme_nombre_acceleration_brusque,
                'somme_nombre_freinage_brusque':somme_nombre_freinage_brusque,
                'somme_nombre_depassement':somme_nombre_depassement,
                
                'somme_nombre_de_malades': somme_nombre_de_malades,
                'somme_violation_des_regles': somme_violation_des_regles,
                'somme_nombre_de_deversement': somme_nombre_de_deversement,
                'somme_volume_de_deversement': somme_volume_de_deversement,
                'somme_surface_impactee': somme_surface_impactee,
                'somme_nombre_inspection': somme_nombre_inspection,
                'somme_zones_de_dechets': somme_zones_de_dechets,
                'somme_zones_de_stockage': somme_zones_de_stockage,
                'somme_dechets_inerte': somme_dechets_inerte,
                'somme_dechets_organique': somme_dechets_organique,
                'somme_dechets_plastique': somme_dechets_plastique,
                'somme_dechets_hydrocarbure': somme_dechets_hydrocarbure,
                'somme_dechets_d3e': somme_dechets_d3e,
                'somme_eaux_usees': somme_eaux_usees,
                'somme_consommation_eau_extraite': somme_consommation_eau_extraite,
                'somme_consommation_de_carburant': somme_consommation_de_carburant,
                'somme_consommation_electricite': somme_consommation_electricite,
                'somme_valeur_limite_seuil': somme_valeur_limite_seuil,
                'somme_x_sur_site': somme_x_sur_site,
                'somme_x_aux_racepteurs': somme_x_aux_racepteurs,
                'somme_x_source_emission': somme_x_source_emission,
                'somme_x_qualite_de_air': somme_x_qualite_de_air,
                'somme_x_sante': somme_x_sante,
                'somme_x_securite': somme_x_securite,
                'somme_x_environnement': somme_x_environnement,
                'somme_x_social': somme_x_social,
                'somme_aucun_incident_social': somme_aucun_incident_social,
                'somme_nombre_de_travailleurs_migrants': somme_nombre_de_travailleurs_migrants,
                'somme_nombre_de_travailleurs_locaux': somme_nombre_de_travailleurs_locaux,
                'somme_pourcentage_main_oeuvre': somme_pourcentage_main_oeuvre,
                'somme_duree_moyenne_travail': somme_duree_moyenne_travail,
                'somme_logement_des_travailleurs': somme_logement_des_travailleurs,
                'somme_approvionnement_eau_potable': somme_approvionnement_eau_potable,
                'somme_nombre_acticivite_engagement': somme_nombre_acticivite_engagement,
                'somme_nombre_activites': somme_nombre_activites,
                'somme_induction_sur_site': somme_induction_sur_site,
                'somme_exercice_urgence': somme_exercice_urgence,
                'somme_toolbox': somme_toolbox,
                'somme_formation_specifique': somme_formation_specifique,
                'somme_starter': somme_starter,
                'somme_nombre_outil_hsses': somme_nombre_outil_hsses,
                'somme_nombre_inspection_hsses': somme_nombre_inspection_hsses,
                'ttl':ttl,
                'ttl1':ttl1
                }
    return render(request, 'KPI/KPI_trans.html', context)

def KPI_stat(request):
    somme_homme, somme_femme, somme_effectif_total_sur_site,somme_heure_travailler,somme_fatalite,somme_accident,somme_poste_adapte,somme_soins_medicaux,somme_premier_secours,somme_presque_accident,somme_dommage_materiel,somme_heure_perdue,somme_km_parcouru,somme_nombre_incident,somme_nombre_acceleration_brusque,somme_nombre_depassement,somme_nombre_freinage_brusque,somme_nombre_de_malades,somme_violation_des_regles,somme_nombre_de_deversement,somme_volume_de_deversement,somme_surface_impactee,somme_nombre_inspection,somme_zones_de_dechets,somme_zones_de_stockage,somme_dechets_inerte,somme_dechets_organique,somme_dechets_plastique,somme_dechets_hydrocarbure,somme_dechets_d3e,somme_eaux_usees,somme_consommation_eau_extraite,somme_consommation_de_carburant,somme_consommation_electricite,somme_valeur_limite_seuil,somme_x_sur_site,somme_x_aux_racepteurs,somme_x_source_emission,somme_x_qualite_de_air,somme_x_sante,somme_x_securite,somme_x_environnement,somme_x_social,somme_aucun_incident_social,somme_nombre_de_travailleurs_migrants,somme_nombre_de_travailleurs_locaux,somme_pourcentage_main_oeuvre,somme_duree_moyenne_travail,somme_logement_des_travailleurs,somme_approvionnement_eau_potable,somme_nombre_acticivite_engagement,somme_nombre_activites,somme_induction_sur_site,somme_exercice_urgence,somme_toolbox,somme_formation_specifique,somme_starter,somme_nombre_outil_hsses,somme_nombre_inspection_hsses, somme_totale = somme_station_service()
    ttl1=somme_totale
    ttl=(somme_totale * 1000000)/somme_effectif_total_sur_site

    if request.method == 'POST':
        start_date = request.POST['start_date']
        end_date = request.POST['end_date']
        events = KPI_station_service.objects.filter(date__range=[start_date, end_date])
        return render(request, 'KPI/KPI_stat.html', {'events':events,
                                                    'somme_homme': somme_homme,
                                                    'somme_femme': somme_femme,
                                                    'somme_effectif_total_sur_site': somme_effectif_total_sur_site,
                                                    'somme_heure_travailler':somme_heure_travailler,
                                                    'somme_fatalite':somme_fatalite,
                                                    'somme_accident':somme_accident,
                                                    'somme_poste_adapte':somme_poste_adapte,
                                                    'somme_soins_medicaux':somme_soins_medicaux,
                                                    'somme_premier_secours':somme_premier_secours,
                                                    'somme_presque_accident':somme_presque_accident,
                                                    'somme_dommage_materiel':somme_dommage_materiel,
                                                    'somme_heure_perdue':somme_heure_perdue,
                                                    'somme_km_parcouru':somme_km_parcouru,
                                                    'somme_km_parcouru':somme_km_parcouru,
                                                    'somme_nombre_incident':somme_nombre_incident,
                                                    'somme_nombre_acceleration_brusque':somme_nombre_acceleration_brusque,
                                                    'somme_nombre_freinage_brusque':somme_nombre_freinage_brusque,
                                                    'somme_nombre_depassement':somme_nombre_depassement,
                                                    
                                                    'somme_nombre_de_malades': somme_nombre_de_malades,
                                                    'somme_violation_des_regles': somme_violation_des_regles,
                                                    'somme_nombre_de_deversement': somme_nombre_de_deversement,
                                                    'somme_volume_de_deversement': somme_volume_de_deversement,
                                                    'somme_surface_impactee': somme_surface_impactee,
                                                    'somme_nombre_inspection': somme_nombre_inspection,
                                                    'somme_zones_de_dechets': somme_zones_de_dechets,
                                                    'somme_zones_de_stockage': somme_zones_de_stockage,
                                                    'somme_dechets_inerte': somme_dechets_inerte,
                                                    'somme_dechets_organique': somme_dechets_organique,
                                                    'somme_dechets_plastique': somme_dechets_plastique,
                                                    'somme_dechets_hydrocarbure': somme_dechets_hydrocarbure,
                                                    'somme_dechets_d3e': somme_dechets_d3e,
                                                    'somme_eaux_usees': somme_eaux_usees,
                                                    'somme_consommation_eau_extraite': somme_consommation_eau_extraite,
                                                    'somme_consommation_de_carburant': somme_consommation_de_carburant,
                                                    'somme_consommation_electricite': somme_consommation_electricite,
                                                    'somme_valeur_limite_seuil': somme_valeur_limite_seuil,
                                                    'somme_x_sur_site': somme_x_sur_site,
                                                    'somme_x_aux_racepteurs': somme_x_aux_racepteurs,
                                                    'somme_x_source_emission': somme_x_source_emission,
                                                    'somme_x_qualite_de_air': somme_x_qualite_de_air,
                                                    'somme_x_sante': somme_x_sante,
                                                    'somme_x_securite': somme_x_securite,
                                                    'somme_x_environnement': somme_x_environnement,
                                                    'somme_x_social': somme_x_social,
                                                    'somme_aucun_incident_social': somme_aucun_incident_social,
                                                    'somme_nombre_de_travailleurs_migrants': somme_nombre_de_travailleurs_migrants,
                                                    'somme_nombre_de_travailleurs_locaux': somme_nombre_de_travailleurs_locaux,
                                                    'somme_pourcentage_main_oeuvre': somme_pourcentage_main_oeuvre,
                                                    'somme_duree_moyenne_travail': somme_duree_moyenne_travail,
                                                    'somme_logement_des_travailleurs': somme_logement_des_travailleurs,
                                                    'somme_approvionnement_eau_potable': somme_approvionnement_eau_potable,
                                                    'somme_nombre_acticivite_engagement': somme_nombre_acticivite_engagement,
                                                    'somme_nombre_activites': somme_nombre_activites,
                                                    'somme_induction_sur_site': somme_induction_sur_site,
                                                    'somme_exercice_urgence': somme_exercice_urgence,
                                                    'somme_toolbox': somme_toolbox,
                                                    'somme_formation_specifique': somme_formation_specifique,
                                                    'somme_starter': somme_starter,
                                                    'somme_nombre_outil_hsses': somme_nombre_outil_hsses,
                                                    'somme_nombre_inspection_hsses': somme_nombre_inspection_hsses,
                                                    'ttl':ttl,
                                                    'ttl1':ttl1
                                                    })
    else:
        events = KPI_station_service.objects.all()
        ttl1=somme_totale
        ttl=(somme_totale * 1000000)/somme_effectif_total_sur_site

    context = { 'events':events,
                'somme_homme': somme_homme,
                'somme_femme': somme_femme,
                'somme_effectif_total_sur_site': somme_effectif_total_sur_site,
                'somme_heure_travailler':somme_heure_travailler,
                'somme_fatalite':somme_fatalite,
                'somme_accident':somme_accident,
                'somme_poste_adapte':somme_poste_adapte,
                'somme_soins_medicaux':somme_soins_medicaux,
                'somme_premier_secours':somme_premier_secours,
                'somme_presque_accident':somme_presque_accident,
                'somme_dommage_materiel':somme_dommage_materiel,
                'somme_heure_perdue':somme_heure_perdue,
                'somme_km_parcouru':somme_km_parcouru,
                'somme_km_parcouru':somme_km_parcouru,
                'somme_nombre_incident':somme_nombre_incident,
                'somme_nombre_acceleration_brusque':somme_nombre_acceleration_brusque,
                'somme_nombre_freinage_brusque':somme_nombre_freinage_brusque,
                'somme_nombre_depassement':somme_nombre_depassement,
                
                'somme_nombre_de_malades': somme_nombre_de_malades,
                'somme_violation_des_regles': somme_violation_des_regles,
                'somme_nombre_de_deversement': somme_nombre_de_deversement,
                'somme_volume_de_deversement': somme_volume_de_deversement,
                'somme_surface_impactee': somme_surface_impactee,
                'somme_nombre_inspection': somme_nombre_inspection,
                'somme_zones_de_dechets': somme_zones_de_dechets,
                'somme_zones_de_stockage': somme_zones_de_stockage,
                'somme_dechets_inerte': somme_dechets_inerte,
                'somme_dechets_organique': somme_dechets_organique,
                'somme_dechets_plastique': somme_dechets_plastique,
                'somme_dechets_hydrocarbure': somme_dechets_hydrocarbure,
                'somme_dechets_d3e': somme_dechets_d3e,
                'somme_eaux_usees': somme_eaux_usees,
                'somme_consommation_eau_extraite': somme_consommation_eau_extraite,
                'somme_consommation_de_carburant': somme_consommation_de_carburant,
                'somme_consommation_electricite': somme_consommation_electricite,
                'somme_valeur_limite_seuil': somme_valeur_limite_seuil,
                'somme_x_sur_site': somme_x_sur_site,
                'somme_x_aux_racepteurs': somme_x_aux_racepteurs,
                'somme_x_source_emission': somme_x_source_emission,
                'somme_x_qualite_de_air': somme_x_qualite_de_air,
                'somme_x_sante': somme_x_sante,
                'somme_x_securite': somme_x_securite,
                'somme_x_environnement': somme_x_environnement,
                'somme_x_social': somme_x_social,
                'somme_aucun_incident_social': somme_aucun_incident_social,
                'somme_nombre_de_travailleurs_migrants': somme_nombre_de_travailleurs_migrants,
                'somme_nombre_de_travailleurs_locaux': somme_nombre_de_travailleurs_locaux,
                'somme_pourcentage_main_oeuvre': somme_pourcentage_main_oeuvre,
                'somme_duree_moyenne_travail': somme_duree_moyenne_travail,
                'somme_logement_des_travailleurs': somme_logement_des_travailleurs,
                'somme_approvionnement_eau_potable': somme_approvionnement_eau_potable,
                'somme_nombre_acticivite_engagement': somme_nombre_acticivite_engagement,
                'somme_nombre_activites': somme_nombre_activites,
                'somme_induction_sur_site': somme_induction_sur_site,
                'somme_exercice_urgence': somme_exercice_urgence,
                'somme_toolbox': somme_toolbox,
                'somme_formation_specifique': somme_formation_specifique,
                'somme_starter': somme_starter,
                'somme_nombre_outil_hsses': somme_nombre_outil_hsses,
                'somme_nombre_inspection_hsses': somme_nombre_inspection_hsses,
                'ttl':ttl,
                'ttl1':ttl1
                }
    return render(request, 'KPI/KPI_stat.html', context)



# KPI AJOUT DE DONNEES

def calcul1(accident, poste, soin, secour, presque, heure):
    if isinstance(accident, (int, float)) and isinstance(poste, (int, float)) and isinstance(soin, (int, float)) and isinstance(secour, (int, float)) and isinstance(presque, (int, float))  and isinstance(heure, (int, float)):
    
        taux_frequence = (((int(accident) + int(poste) + int(soin) + int(secour) + int(presque) ) * 1000000) / int(heure))
        return taux_frequence
    else:
        return None
        
def calcul2(accident, poste, soin, secour, presque ,heure):
    if isinstance(accident, (int, float)) and isinstance(poste, (int, float)) and isinstance(soin, (int, float)) and isinstance(secour, (int, float)) and isinstance(presque, (int, float))  and isinstance(heure, (int, float)):
        taux_frequence = (((int(accident) + int(poste) + int(soin) + int(secour )+ int(presque) ) * 1000) / int(heure))
        return taux_frequence
    else:
        return None
    
def calcul3(perdue , travail):
    if isinstance(perdue,(int,float)) and isinstance(travail,(int,float)):
        taux_gravite = (((int(perdue) * 1000)/int(travail)))
        return taux_gravite  
    else:
        return None

def KPI_jov_ajout(request):
    if request.method == 'POST':
        form = KPI_jovenaForm(request.POST)
        
        
        if form.is_valid():
            data = form.cleaned_data  # Extraire les données du formulaire
            
            date = data['date']
            mois = date.strftime('%B').lower()
            
            
            if mois =='january':
                taux_frequence_incident = calcul1(int(data['accident']), int(data['poste_adapte']), int(data['soins_medicaux']), int(data['premier_secours']), int(data['presque_accident']), int(data['heure_travailler']))
            else:
                taux_frequence_incident = calcul2(int(data['accident']), int(data['poste_adapte']), int(data['soins_medicaux']), int(data['premier_secours']), int(data['presque_accident']), int(data['heure_travailler']))

            if mois=='january':
                taux_gravite_incident = 0 
            else:
                taux_gravite_incident = calcul3(int(data['heure_perdue']), int(data['heure_travailler']))
            
            kpi = form.save()
            
            kpi.taux_frequence_incident = taux_frequence_incident  # Associez la valeur calculée au champ du modèle
            kpi.taux_gravite_incident = taux_gravite_incident
            kpi.save()
            
            messages.success(request, 'REUSSI')
            print(kpi.taux_frequence_incident, kpi.taux_gravite_incident)
            return redirect('KPI_jov_ajout')
        else:
            messages.error(request, 'Tsy mety')
            print(messages.error)
            return redirect('KPI_jov_ajout')
    else:
        form = KPI_jovenaForm(request.user)
        
    context = {'form':form}
    
    #context = {}
    return render(request, 'KPI/Ajout/donnee_jov.html', context)

def KPI_prest_ajout(request):
    if request.method == 'POST':
        form = KPI_prestataireForm(request.POST)
        
        
        if form.is_valid():
            data = form.cleaned_data  # Extraire les données du formulaire
            
            date = data['date']
            mois = date.strftime('%B').lower()
            
            
            if mois =='january':
                taux_frequence_incident = calcul1(int(data['accident']), int(data['poste_adapte']), int(data['soins_medicaux']), int(data['premier_secours']), int(data['presque_accident']), int(data['heure_travailler']))
            else:
                taux_frequence_incident = calcul2(int(data['accident']), int(data['poste_adapte']), int(data['soins_medicaux']), int(data['premier_secours']), int(data['presque_accident']), int(data['heure_travailler']))

            if mois=='january':
                taux_gravite_incident = 0 
            else:
                taux_gravite_incident = calcul3(int(data['heure_perdue']), int(data['heure_travailler']))
            
            kpi = form.save()
            
            kpi.taux_frequence_incident = taux_frequence_incident  # Associez la valeur calculée au champ du modèle
            kpi.taux_gravite_incident = taux_gravite_incident
            kpi.save()
            
            messages.success(request, 'REUSSI')
            print(kpi.taux_frequence_incident, kpi.taux_gravite_incident)
            return redirect('KPI_prest_ajout')
        else:
            messages.error(request, 'Tsy mety')
            print(messages.error)
            return redirect('KPI_prest_ajout')
    else:
        form = KPI_jovenaForm(request.user)
        
    context = {'form':form}
    
    #context = {}
    return render(request, 'KPI/Ajout/donnee_prest.html', context)

def KPI_trans_ajout(request):
    
    if request.method == 'POST':
        form = KPI_transporteurForm(request.POST)
        
        
        if form.is_valid():
            data = form.cleaned_data  # Extraire les données du formulaire
            
            date = data['date']
            mois = date.strftime('%B').lower()
            
            
            if mois =='january':
                taux_frequence_incident = calcul1(int(data['accident']), int(data['poste_adapte']), int(data['soins_medicaux']), int(data['premier_secours']), int(data['presque_accident']), int(data['heure_travailler']))
            else:
                taux_frequence_incident = calcul2(int(data['accident']), int(data['poste_adapte']), int(data['soins_medicaux']), int(data['premier_secours']), int(data['presque_accident']), int(data['heure_travailler']))

            if mois=='january':
                taux_gravite_incident = 0 
            else:
                taux_gravite_incident = calcul3(int(data['heure_perdue']), int(data['heure_travailler']))
            
            kpi = form.save()
            
            kpi.taux_frequence_incident = taux_frequence_incident  # Associez la valeur calculée au champ du modèle
            kpi.taux_gravite_incident = taux_gravite_incident
            kpi.save()
            
            messages.success(request, 'REUSSI')
            print(kpi.taux_frequence_incident, kpi.taux_gravite_incident)
            return redirect('KPI_trans_ajout')
        else:
            messages.error(request, 'Tsy mety')
            print(messages.error)
            return redirect('KPI_trans_ajout')
    else:
        form = KPI_jovenaForm(request.user)
        
    context = {'form':form}
    
    return render(request, 'KPI/Ajout/donnee_trans.html', context)

def KPI_stat_ajout(request):
    
    if request.method == 'POST':
        form = KPI_station_serviceForm(request.POST)
        
        if form.is_valid():
            data = form.cleaned_data  # Extraire les données du formulaire
            
            date = data['date']
            mois = date.strftime('%B').lower()
            
            if mois =='january':
                taux_frequence_incident = calcul1(int(data['accident']), int(data['poste_adapte']), int(data['soins_medicaux']), int(data['premier_secours']), int(data['presque_accident']), int(data['heure_travailler']))
            else:
                taux_frequence_incident = calcul2(int(data['accident']), int(data['poste_adapte']), int(data['soins_medicaux']), int(data['premier_secours']), int(data['presque_accident']), int(data['heure_travailler']))

            if mois=='january':
                taux_gravite_incident = 0 
            else:
                taux_gravite_incident = calcul3(int(data['heure_perdue']), int(data['heure_travailler']))
            
            kpi = form.save()
            
            kpi.taux_frequence_incident = taux_frequence_incident  # Associez la valeur calculée au champ du modèle
            kpi.taux_gravite_incident = taux_gravite_incident
            kpi.save()
            
            messages.success(request, 'REUSSI')
            print(kpi.taux_frequence_incident, kpi.taux_gravite_incident)
            return redirect('KPI_stat_ajout')
        else:
            messages.error(request, 'Tsy mety')
            print(messages.error)
            return redirect('KPI_stat_ajout')
    else:
        form = KPI_jovenaForm(request.user)
        
    context = {'form':form}
    
    return render(request, 'KPI/Ajout/donnee_stat.html', context)

def message_prest_views(request):
    validations = checklist_permis_feu_prest.objects.values('validation','user_profile_feu','date_entete')
    validations2 = checklist_espace_confinez.objects.values('validation','user_profile_confine','date_entete')
    validations3 = checklist_excavation.objects.values('validation','user_profile_excavation','date_entete')

    # Maintenant, vous pouvez utiliser la variable 'validation' dans votre contexte
    context = {
        'validations': validations,
        'validations2': validations2,
        'validations3': validations3,

    }
    
    return render(request, 'message/message_prest.html', context)