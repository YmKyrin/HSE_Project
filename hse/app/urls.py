from django.urls import path
from . import views

urlpatterns = [
    # App
    path('login/', views.loginPage, name='login'),
    path('logoutUser/', views.logoutUser, name='logoutUser'),
    
    # Accueil
    path('Accueil_jovena/', views.accueil_jov, name='accueil_jov'),
    path('Accueil_prestataire/', views.accueil_prest, name='accueil_prest'),
    path('Accueil_station_service/', views.accueil_stat, name='accueil_stat'),
    path('Accueil_transporteur/', views.accueil_trans, name='accueil_trans'),
    
    # Base Documentaire
    path('BD_jovena/', views.BD_jov, name='BD_jov'),
    path('BD_prestataire/', views.BD_prest, name='BD_prest'),
    path('BD_station_service/', views.BD_stat, name='BD_stat'),
    path('BD_transporteur/', views.BD_trans, name='BD_trans'),
    
    # Politique
    path('Politique_jovena/', views.politique_jov, name='politique_jov'),
    path('Politique_prestataire/', views.politique_prest, name='politique_prest'),
    path('Politique_station_service/', views.politique_stat, name='politique_stat'),
    path('Politique_transporteur/', views.politique_trans, name='politique_trans'),
    
    # Registre des incidents
    path('Incident_jovena/', views.incident_jov, name='incident_jov'),
    path('Incident_prestataire/', views.incident_prest, name='incident_prest'),
    path('Incident_station_service/', views.incident_stat, name='incident_stat'),
    path('Incident_transporteur/', views.incident_trans, name='incident_trans'),
    
    # Indicateurs
    path('Indicateur_jovena/', views.indicateur_jov, name='indicateur_jov'),
    path('Indicateur_prestataire/', views.indicateur_prest, name='indicateur_prest'),
    path('Indicateur_station_service/', views.indicateur_stat, name='indicateur_stat'),
    path('Indicateur_transporteur/', views.indicateur_trans, name='indicateur_trans'),
    
    # Equipement
    path('Equipement_jovena/', views.equip_jov, name='equip_jov'),
    path('Equipement_prestataire/', views.equip_prest, name='equip_prest'),
    path('Equipement_station_service/', views.equip_stat, name='equip_stat'),
    path('Equipement_transporteur/', views.equip_trans, name='equip_trans'),
    
    # Base de Donnée (informations)
    path('Information_jovena/', views.info_jov, name='info_jov'),
    path('Information_prestataire/', views.info_prest, name='info_prest'),
    path('Information_station_service/', views.info_stat, name='info_stat'),
    path('Information_transporteur/', views.info_trans, name='info_trans'),
    
    # Checklist
    path('Checklist_jovena/', views.checklist_jov, name='checklist_jov'),
    path('Checklist_prestataire/', views.checklist_prest, name='checklist_prest'),
    path('Checklist_station_service/', views.checklist_stat, name='checklist_stat'),
    path('Checklist_transporteur/', views.checklist_trans, name='checklist_trans'),
    
    # path('Checklist_permis_feu_prest/', views.checklist_permis_feu_prest, name='checklist_permis_feu_prest'),
    path('Checklist_permis_excavation_prest/', views.checklist_excavation_prest, name='checklist_permis_excavation_prest'),
    path('Checklist_espace_confine_prest/', views.checklist_espace_confine, name='checklist_espace_confine_prest'),
    
    # Parametre
    path('Parametre_jovena/', views.parametre_jov, name='parametre_jov'),
    path('Parametre_prestataire/', views.parametre_prest, name='parametre_prest'),
    path('Parametre_station_service/', views.parametre_stat, name='parametre_stat'),
    path('Parametre_transporteur/', views.parametre_trans, name='parametre_trans'),
    
    # KPI
    path('KPI_jovena/', views.KPI_jov, name='KPI_jov'),
    path('KPI_prestataire/', views.KPI_prest, name='KPI_prest'),
    path('KPI_station_service/', views.KPI_stat, name='KPI_stat'),
    path('KPI_transporteur/', views.KPI_trans, name='KPI_trans'),
    
    # KPI / Ajout de donnees
    path('KPI_jovena_ajout/', views.KPI_jov_ajout, name='KPI_jov_ajout'),
    path('KPI_prestataire_ajout/', views.KPI_prest_ajout, name='KPI_prest_ajout'),
    path('KPI_station_service_ajout/', views.KPI_stat_ajout, name='KPI_stat_ajout'),
    path('KPI_transporteur_ajout/', views.KPI_trans_ajout, name='KPI_trans_ajout'),
    
    # MESSAGE
    path('Message_prestataire/', views.message_prest_views, name = 'message_prest')
    
    #pdf
     
    
]
