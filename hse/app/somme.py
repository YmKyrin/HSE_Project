from app.models import *
from django.db.models import Sum


# def somme_hommes():
#     somme = KPI_jovena.objects.aggregate(total_hommes=Sum('homme'))
#     total_hommes = somme['total_hommes'] if somme['total_hommes'] is not None else 0
#     return total_hommes  # Retourne la somme

def somme_jovena():
    sommes = KPI_jovena.objects.aggregate(
        somme_homme=Sum('homme'),
        somme_femme=Sum('femme'),
        somme_effectif_total_sur_site=Sum('effectif_total_sur_site'),
        somme_heure_travailler=Sum('heure_travailler'),
        somme_fatalite=Sum('fatalite'),
        somme_accident=Sum('accident'),
        somme_poste_adapte=Sum('poste_adapte'),
        somme_soins_medicaux=Sum('soins_medicaux'),
        somme_premier_secours=Sum('premier_secours'),
        somme_presque_accident=Sum('presque_accident'),
        somme_dommage_materiel=Sum('dommage_materiel'),
        somme_heure_perdue=Sum('heure_perdue'),
        somme_km_parcouru=Sum('km_parcouru'),
        somme_nombre_incident=Sum('nombre_incident'),
        somme_nombre_acceleration_brusque=Sum('nombre_acceleration_brusque'),
        somme_nombre_freinage_brusque=Sum('nombre_freinage_brusque'),
        somme_nombre_depassement=Sum('nombre_depassement'),
        
        
        somme_nombre_de_malades=Sum('nombre_de_malades'),
        somme_violation_des_regles=Sum('violation_des_regles'),
        somme_nombre_de_deversement=Sum('nombre_de_deversement'),
        somme_volume_de_deversement=Sum('volume_de_deversement'),
        somme_surface_impactee=Sum('surface_impactee'),
        somme_nombre_inspection=Sum('nombre_inspection'),
        somme_zones_de_dechets=Sum('zones_de_dechets'),
        somme_zones_de_stockage=Sum('zones_de_stockage'),
        somme_dechets_inerte=Sum('dechets_inerte'),
        somme_dechets_organique=Sum('dechets_organique'),
        somme_dechets_plastique=Sum('dechets_plastique'),
        somme_dechets_hydrocarbure=Sum('dechets_hydrocarbure'),
        somme_dechets_d3e=Sum('dechets_d3e'),
        somme_eaux_usees=Sum('eaux_usees'),
        somme_consommation_eau_extraite=Sum('consommation_eau_extraite'),
        somme_consommation_de_carburant=Sum('consommation_de_carburant'),
        somme_consommation_electricite=Sum('consommation_electricite'),
        somme_valeur_limite_seuil=Sum('valeur_limite_seuil'),
        somme_x_sur_site=Sum('x_sur_site'),
        somme_x_aux_racepteurs=Sum('x_aux_racepteurs'),
        somme_x_source_emission=Sum('x_source_emission'),
        somme_x_qualite_de_air=Sum('x_qualite_de_air'),
        somme_x_sante=Sum('x_sante'),
        somme_x_securite=Sum('x_securite'),
        somme_x_environnement=Sum('x_environnement'),
        somme_x_social=Sum('x_social'),
        somme_aucun_incident_social=Sum('aucun_incident_social'),
        somme_nombre_de_travailleurs_migrants=Sum('nombre_de_travailleurs_migrants'),
        somme_nombre_de_travailleurs_locaux=Sum('nombre_de_travailleurs_locaux'),
        somme_pourcentage_main_oeuvre=Sum('pourcentage_main_oeuvre'),
        somme_duree_moyenne_travail=Sum('duree_moyenne_travail'),
        somme_logement_des_travailleurs=Sum('logement_des_travailleurs'),
        somme_approvionnement_eau_potable=Sum('approvionnement_eau_potable'),
        somme_nombre_acticivite_engagement=Sum('nombre_acticivite_engagement'),
        somme_nombre_activites=Sum('nombre_activites'),
        somme_induction_sur_site=Sum('induction_sur_site'),
        somme_exercice_urgence=Sum('exercice_urgence'),
        somme_toolbox=Sum('toolbox'),
        somme_formation_specifique=Sum('formation_specifique'),
        somme_starter=Sum('starter'),
        somme_nombre_outil_hsses=Sum('nombre_outil_hsses'),
        somme_nombre_inspection_hsses=Sum('nombre_inspection_hsses'),
        
    )
    
    somme_homme = sommes['somme_homme'] if sommes['somme_homme'] is not None else 0
    somme_femme = sommes['somme_femme'] if sommes['somme_femme'] is not None else 0
    somme_effectif_total_sur_site = sommes['somme_effectif_total_sur_site'] if sommes['somme_effectif_total_sur_site'] is not None else 1
    somme_heure_travailler=sommes['somme_heure_travailler']if sommes['somme_heure_travailler'] is not None else 0
    somme_fatalite=sommes['somme_fatalite']if sommes['somme_fatalite'] is not None else 0
    somme_accident=sommes['somme_accident']if sommes['somme_accident'] is not None else 0
    somme_poste_adapte=sommes['somme_poste_adapte']if sommes['somme_poste_adapte'] is not None else 0
    somme_soins_medicaux=sommes['somme_soins_medicaux']if sommes['somme_soins_medicaux'] is not None else 0
    somme_premier_secours=sommes['somme_premier_secours']if sommes['somme_premier_secours'] is not None else 0
    somme_presque_accident=sommes['somme_presque_accident']if sommes['somme_presque_accident'] is not None else 0
    somme_dommage_materiel=sommes['somme_dommage_materiel']if sommes['somme_dommage_materiel'] is not None else 0
    somme_heure_perdue=sommes['somme_heure_perdue']if sommes['somme_heure_perdue'] is not None else 0
    somme_km_parcouru=sommes['somme_km_parcouru']if sommes['somme_km_parcouru'] is not None else 0
    somme_nombre_incident=sommes['somme_nombre_incident']if sommes['somme_nombre_incident'] is not None else 0
    somme_nombre_acceleration_brusque=sommes['somme_nombre_acceleration_brusque']if sommes['somme_nombre_acceleration_brusque'] is not None else 0
    somme_nombre_freinage_brusque=sommes['somme_nombre_freinage_brusque']if sommes['somme_nombre_freinage_brusque'] is not None else 0
    somme_nombre_depassement=sommes['somme_nombre_depassement']if sommes['somme_nombre_depassement'] is not None else 0
    
    
    somme_nombre_de_malades=sommes['somme_nombre_de_malades'] if sommes['somme_nombre_de_malades'] is not None else 0
    somme_violation_des_regles=sommes['somme_violation_des_regles'] if sommes['somme_violation_des_regles'] is not None else 0
    somme_nombre_de_deversement=sommes['somme_nombre_de_deversement'] if sommes['somme_nombre_de_deversement'] is not None else 0
    somme_volume_de_deversement=sommes['somme_volume_de_deversement'] if sommes['somme_volume_de_deversement'] is not None else 0
    somme_surface_impactee=sommes['somme_surface_impactee'] if sommes['somme_surface_impactee'] is not None else 0
    somme_nombre_inspection=sommes['somme_nombre_inspection'] if sommes['somme_nombre_inspection'] is not None else 0
    somme_zones_de_dechets=sommes['somme_zones_de_dechets'] if sommes['somme_zones_de_dechets'] is not None else 0
    somme_zones_de_stockage=sommes['somme_zones_de_stockage'] if sommes['somme_zones_de_stockage'] is not None else 0
    somme_dechets_inerte=sommes['somme_dechets_inerte'] if sommes['somme_dechets_inerte'] is not None else 0
    somme_dechets_organique=sommes['somme_dechets_organique'] if sommes['somme_dechets_organique'] is not None else 0
    somme_dechets_plastique=sommes['somme_dechets_plastique'] if sommes['somme_dechets_plastique'] is not None else 0
    somme_dechets_hydrocarbure=sommes['somme_dechets_hydrocarbure'] if sommes['somme_dechets_hydrocarbure'] is not None else 0
    somme_dechets_d3e=sommes['somme_dechets_d3e'] if sommes['somme_dechets_d3e'] is not None else 0
    somme_eaux_usees=sommes['somme_eaux_usees'] if sommes['somme_eaux_usees'] is not None else 0
    somme_consommation_eau_extraite=sommes['somme_consommation_eau_extraite'] if sommes['somme_consommation_eau_extraite'] is not None else 0
    somme_consommation_de_carburant=sommes['somme_consommation_de_carburant'] if sommes['somme_consommation_de_carburant'] is not None else 0
    somme_consommation_electricite=sommes['somme_consommation_electricite'] if sommes['somme_consommation_electricite'] is not None else 0
    somme_valeur_limite_seuil=sommes['somme_valeur_limite_seuil'] if sommes['somme_valeur_limite_seuil'] is not None else 0
    somme_x_sur_site=sommes['somme_x_sur_site'] if sommes['somme_x_sur_site'] is not None else 0
    somme_x_aux_racepteurs=sommes['somme_x_aux_racepteurs'] if sommes['somme_x_aux_racepteurs'] is not None else 0
    somme_x_source_emission=sommes['somme_x_source_emission'] if sommes['somme_x_source_emission'] is not None else 0
    somme_x_qualite_de_air=sommes['somme_x_qualite_de_air'] if sommes['somme_x_qualite_de_air'] is not None else 0
    somme_x_sante=sommes['somme_x_sante'] if sommes['somme_x_sante'] is not None else 0
    somme_x_securite=sommes['somme_x_securite'] if sommes['somme_x_securite'] is not None else 0
    somme_x_environnement=sommes['somme_x_environnement'] if sommes['somme_x_environnement'] is not None else 0
    somme_x_social=sommes['somme_x_social'] if sommes['somme_x_social'] is not None else 0
    somme_aucun_incident_social=sommes['somme_aucun_incident_social'] if sommes['somme_aucun_incident_social'] is not None else 0
    somme_nombre_de_travailleurs_migrants=sommes['somme_nombre_de_travailleurs_migrants'] if sommes['somme_nombre_de_travailleurs_migrants'] is not None else 0
    somme_nombre_de_travailleurs_locaux=sommes['somme_nombre_de_travailleurs_locaux'] if sommes['somme_nombre_de_travailleurs_locaux'] is not None else 0
    somme_pourcentage_main_oeuvre=sommes['somme_pourcentage_main_oeuvre'] if sommes['somme_pourcentage_main_oeuvre'] is not None else 0
    somme_duree_moyenne_travail=sommes['somme_duree_moyenne_travail'] if sommes['somme_duree_moyenne_travail'] is not None else 0
    somme_logement_des_travailleurs=sommes['somme_logement_des_travailleurs'] if sommes['somme_logement_des_travailleurs'] is not None else 0
    somme_approvionnement_eau_potable=sommes['somme_approvionnement_eau_potable'] if sommes['somme_approvionnement_eau_potable'] is not None else 0
    somme_nombre_acticivite_engagement=sommes['somme_nombre_acticivite_engagement'] if sommes['somme_nombre_acticivite_engagement'] is not None else 0
    somme_nombre_activites=sommes['somme_nombre_activites'] if sommes['somme_nombre_activites'] is not None else 0
    somme_induction_sur_site=sommes['somme_induction_sur_site'] if sommes['somme_induction_sur_site'] is not None else 0
    somme_exercice_urgence=sommes['somme_exercice_urgence'] if sommes['somme_exercice_urgence'] is not None else 0
    somme_toolbox=sommes['somme_toolbox'] if sommes['somme_toolbox'] is not None else 0
    somme_formation_specifique=sommes['somme_formation_specifique'] if sommes['somme_formation_specifique'] is not None else 0
    somme_starter=sommes['somme_starter'] if sommes['somme_starter'] is not None else 0
    somme_nombre_outil_hsses=sommes['somme_nombre_outil_hsses'] if sommes['somme_nombre_outil_hsses'] is not None else 0
    somme_nombre_inspection_hsses=sommes['somme_nombre_inspection_hsses'] if sommes['somme_nombre_inspection_hsses'] is not None else 0
    
    somme_totale = somme_homme + somme_femme + somme_effectif_total_sur_site + somme_heure_travailler + somme_fatalite + somme_accident + somme_poste_adapte + somme_soins_medicaux + somme_premier_secours + somme_presque_accident + somme_dommage_materiel + somme_heure_perdue + somme_km_parcouru + somme_nombre_incident + somme_nombre_acceleration_brusque + somme_nombre_depassement + somme_nombre_freinage_brusque + somme_nombre_de_malades + somme_violation_des_regles + somme_nombre_de_deversement + somme_volume_de_deversement + somme_surface_impactee + somme_nombre_inspection + somme_zones_de_dechets + somme_zones_de_stockage + somme_dechets_inerte + somme_dechets_organique + somme_dechets_plastique + somme_dechets_hydrocarbure + somme_dechets_d3e + somme_eaux_usees + somme_consommation_eau_extraite + somme_consommation_de_carburant + somme_consommation_electricite + somme_valeur_limite_seuil + somme_x_sur_site + somme_x_aux_racepteurs + somme_x_source_emission + somme_x_qualite_de_air + somme_x_sante + somme_x_securite + somme_x_environnement + somme_x_social + somme_aucun_incident_social + somme_nombre_de_travailleurs_migrants + somme_nombre_de_travailleurs_locaux + somme_pourcentage_main_oeuvre + somme_duree_moyenne_travail + somme_logement_des_travailleurs + somme_approvionnement_eau_potable + somme_nombre_acticivite_engagement + somme_nombre_activites + somme_induction_sur_site + somme_exercice_urgence + somme_toolbox + somme_formation_specifique + somme_starter + somme_nombre_outil_hsses + somme_nombre_inspection_hsses

    
    return somme_homme, somme_femme, somme_effectif_total_sur_site,somme_heure_travailler,somme_fatalite,somme_accident,somme_poste_adapte,somme_soins_medicaux,somme_premier_secours,somme_presque_accident,somme_dommage_materiel,somme_heure_perdue,somme_km_parcouru,somme_nombre_incident,somme_nombre_acceleration_brusque,somme_nombre_depassement,somme_nombre_freinage_brusque,somme_nombre_de_malades,somme_violation_des_regles,somme_nombre_de_deversement,somme_volume_de_deversement,somme_surface_impactee,somme_nombre_inspection,somme_zones_de_dechets,somme_zones_de_stockage,somme_dechets_inerte,somme_dechets_organique,somme_dechets_plastique,somme_dechets_hydrocarbure,somme_dechets_d3e,somme_eaux_usees,somme_consommation_eau_extraite,somme_consommation_de_carburant,somme_consommation_electricite,somme_valeur_limite_seuil,somme_x_sur_site,somme_x_aux_racepteurs,somme_x_source_emission,somme_x_qualite_de_air,somme_x_sante,somme_x_securite,somme_x_environnement,somme_x_social,somme_aucun_incident_social,somme_nombre_de_travailleurs_migrants,somme_nombre_de_travailleurs_locaux,somme_pourcentage_main_oeuvre,somme_duree_moyenne_travail,somme_logement_des_travailleurs,somme_approvionnement_eau_potable,somme_nombre_acticivite_engagement,somme_nombre_activites,somme_induction_sur_site,somme_exercice_urgence,somme_toolbox,somme_formation_specifique,somme_starter,somme_nombre_outil_hsses,somme_nombre_inspection_hsses,somme_totale


def somme_prestataire():
    sommes = KPI_prestataire.objects.aggregate(
        somme_homme=Sum('homme'),
        somme_femme=Sum('femme'),
        somme_effectif_total_sur_site=Sum('effectif_total_sur_site'),
        somme_heure_travailler=Sum('heure_travailler'),
        somme_fatalite=Sum('fatalite'),
        somme_accident=Sum('accident'),
        somme_poste_adapte=Sum('poste_adapte'),
        somme_soins_medicaux=Sum('soins_medicaux'),
        somme_premier_secours=Sum('premier_secours'),
        somme_presque_accident=Sum('presque_accident'),
        somme_dommage_materiel=Sum('dommage_materiel'),
        somme_heure_perdue=Sum('heure_perdue'),
        somme_km_parcouru=Sum('km_parcouru'),
        somme_nombre_incident=Sum('nombre_incident'),
        somme_nombre_acceleration_brusque=Sum('nombre_acceleration_brusque'),
        somme_nombre_freinage_brusque=Sum('nombre_freinage_brusque'),
        somme_nombre_depassement=Sum('nombre_depassement'),
        somme_nombre_de_malades=Sum('nombre_de_malades'),
        somme_violation_des_regles=Sum('violation_des_regles'),
        somme_nombre_de_deversement=Sum('nombre_de_deversement'),
        somme_volume_de_deversement=Sum('volume_de_deversement'),
        somme_surface_impactee=Sum('surface_impactee'),
        somme_nombre_inspection=Sum('nombre_inspection'),
        somme_zones_de_dechets=Sum('zones_de_dechets'),
        somme_zones_de_stockage=Sum('zones_de_stockage'),
        somme_dechets_inerte=Sum('dechets_inerte'),
        somme_dechets_organique=Sum('dechets_organique'),
        somme_dechets_plastique=Sum('dechets_plastique'),
        somme_dechets_hydrocarbure=Sum('dechets_hydrocarbure'),
        somme_dechets_d3e=Sum('dechets_d3e'),
        somme_eaux_usees=Sum('eaux_usees'),
        somme_consommation_eau_extraite=Sum('consommation_eau_extraite'),
        somme_consommation_de_carburant=Sum('consommation_de_carburant'),
        somme_consommation_electricite=Sum('consommation_electricite'),
        somme_valeur_limite_seuil=Sum('valeur_limite_seuil'),
        somme_x_sur_site=Sum('x_sur_site'),
        somme_x_aux_racepteurs=Sum('x_aux_racepteurs'),
        somme_x_source_emission=Sum('x_source_emission'),
        somme_x_qualite_de_air=Sum('x_qualite_de_air'),
        somme_x_sante=Sum('x_sante'),
        somme_x_securite=Sum('x_securite'),
        somme_x_environnement=Sum('x_environnement'),
        somme_x_social=Sum('x_social'),
        somme_aucun_incident_social=Sum('aucun_incident_social'),
        somme_nombre_de_travailleurs_migrants=Sum('nombre_de_travailleurs_migrants'),
        somme_nombre_de_travailleurs_locaux=Sum('nombre_de_travailleurs_locaux'),
        somme_pourcentage_main_oeuvre=Sum('pourcentage_main_oeuvre'),
        somme_duree_moyenne_travail=Sum('duree_moyenne_travail'),
        somme_logement_des_travailleurs=Sum('logement_des_travailleurs'),
        somme_approvionnement_eau_potable=Sum('approvionnement_eau_potable'),
        somme_nombre_acticivite_engagement=Sum('nombre_acticivite_engagement'),
        somme_nombre_activites=Sum('nombre_activites'),
        somme_induction_sur_site=Sum('induction_sur_site'),
        somme_exercice_urgence=Sum('exercice_urgence'),
        somme_toolbox=Sum('toolbox'),
        somme_formation_specifique=Sum('formation_specifique'),
        somme_starter=Sum('starter'),
        somme_nombre_outil_hsses=Sum('nombre_outil_hsses'),
        somme_nombre_inspection_hsses=Sum('nombre_inspection_hsses'),
        
    )
    
    somme_homme = sommes['somme_homme'] if sommes['somme_homme'] is not None else 0
    somme_femme = sommes['somme_femme'] if sommes['somme_femme'] is not None else 0
    somme_effectif_total_sur_site = sommes['somme_effectif_total_sur_site'] if sommes['somme_effectif_total_sur_site'] is not None else 1
    somme_heure_travailler=sommes['somme_heure_travailler']if sommes['somme_heure_travailler'] is not None else 0
    somme_fatalite=sommes['somme_fatalite']if sommes['somme_fatalite'] is not None else 0
    somme_accident=sommes['somme_accident']if sommes['somme_accident'] is not None else 0
    somme_poste_adapte=sommes['somme_poste_adapte']if sommes['somme_poste_adapte'] is not None else 0
    somme_soins_medicaux=sommes['somme_soins_medicaux']if sommes['somme_soins_medicaux'] is not None else 0
    somme_premier_secours=sommes['somme_premier_secours']if sommes['somme_premier_secours'] is not None else 0
    somme_presque_accident=sommes['somme_presque_accident']if sommes['somme_presque_accident'] is not None else 0
    somme_dommage_materiel=sommes['somme_dommage_materiel']if sommes['somme_dommage_materiel'] is not None else 0
    somme_heure_perdue=sommes['somme_heure_perdue']if sommes['somme_heure_perdue'] is not None else 0
    somme_km_parcouru=sommes['somme_km_parcouru']if sommes['somme_km_parcouru'] is not None else 0
    somme_nombre_incident=sommes['somme_nombre_incident']if sommes['somme_nombre_incident'] is not None else 0
    somme_nombre_acceleration_brusque=sommes['somme_nombre_acceleration_brusque']if sommes['somme_nombre_acceleration_brusque'] is not None else 0
    somme_nombre_freinage_brusque=sommes['somme_nombre_freinage_brusque']if sommes['somme_nombre_freinage_brusque'] is not None else 0
    somme_nombre_depassement=sommes['somme_nombre_depassement']if sommes['somme_nombre_depassement'] is not None else 0
    
    somme_nombre_de_malades=sommes['somme_nombre_de_malades'] if sommes['somme_nombre_de_malades'] is not None else 0
    somme_violation_des_regles=sommes['somme_violation_des_regles'] if sommes['somme_violation_des_regles'] is not None else 0
    somme_nombre_de_deversement=sommes['somme_nombre_de_deversement'] if sommes['somme_nombre_de_deversement'] is not None else 0
    somme_volume_de_deversement=sommes['somme_volume_de_deversement'] if sommes['somme_volume_de_deversement'] is not None else 0
    somme_surface_impactee=sommes['somme_surface_impactee'] if sommes['somme_surface_impactee'] is not None else 0
    somme_nombre_inspection=sommes['somme_nombre_inspection'] if sommes['somme_nombre_inspection'] is not None else 0
    somme_zones_de_dechets=sommes['somme_zones_de_dechets'] if sommes['somme_zones_de_dechets'] is not None else 0
    somme_zones_de_stockage=sommes['somme_zones_de_stockage'] if sommes['somme_zones_de_stockage'] is not None else 0
    somme_dechets_inerte=sommes['somme_dechets_inerte'] if sommes['somme_dechets_inerte'] is not None else 0
    somme_dechets_organique=sommes['somme_dechets_organique'] if sommes['somme_dechets_organique'] is not None else 0
    somme_dechets_plastique=sommes['somme_dechets_plastique'] if sommes['somme_dechets_plastique'] is not None else 0
    somme_dechets_hydrocarbure=sommes['somme_dechets_hydrocarbure'] if sommes['somme_dechets_hydrocarbure'] is not None else 0
    somme_dechets_d3e=sommes['somme_dechets_d3e'] if sommes['somme_dechets_d3e'] is not None else 0
    somme_eaux_usees=sommes['somme_eaux_usees'] if sommes['somme_eaux_usees'] is not None else 0
    somme_consommation_eau_extraite=sommes['somme_consommation_eau_extraite'] if sommes['somme_consommation_eau_extraite'] is not None else 0
    somme_consommation_de_carburant=sommes['somme_consommation_de_carburant'] if sommes['somme_consommation_de_carburant'] is not None else 0
    somme_consommation_electricite=sommes['somme_consommation_electricite'] if sommes['somme_consommation_electricite'] is not None else 0
    somme_valeur_limite_seuil=sommes['somme_valeur_limite_seuil'] if sommes['somme_valeur_limite_seuil'] is not None else 0
    somme_x_sur_site=sommes['somme_x_sur_site'] if sommes['somme_x_sur_site'] is not None else 0
    somme_x_aux_racepteurs=sommes['somme_x_aux_racepteurs'] if sommes['somme_x_aux_racepteurs'] is not None else 0
    somme_x_source_emission=sommes['somme_x_source_emission'] if sommes['somme_x_source_emission'] is not None else 0
    somme_x_qualite_de_air=sommes['somme_x_qualite_de_air'] if sommes['somme_x_qualite_de_air'] is not None else 0
    somme_x_sante=sommes['somme_x_sante'] if sommes['somme_x_sante'] is not None else 0
    somme_x_securite=sommes['somme_x_securite'] if sommes['somme_x_securite'] is not None else 0
    somme_x_environnement=sommes['somme_x_environnement'] if sommes['somme_x_environnement'] is not None else 0
    somme_x_social=sommes['somme_x_social'] if sommes['somme_x_social'] is not None else 0
    somme_aucun_incident_social=sommes['somme_aucun_incident_social'] if sommes['somme_aucun_incident_social'] is not None else 0
    somme_nombre_de_travailleurs_migrants=sommes['somme_nombre_de_travailleurs_migrants'] if sommes['somme_nombre_de_travailleurs_migrants'] is not None else 0
    somme_nombre_de_travailleurs_locaux=sommes['somme_nombre_de_travailleurs_locaux'] if sommes['somme_nombre_de_travailleurs_locaux'] is not None else 0
    somme_pourcentage_main_oeuvre=sommes['somme_pourcentage_main_oeuvre'] if sommes['somme_pourcentage_main_oeuvre'] is not None else 0
    somme_duree_moyenne_travail=sommes['somme_duree_moyenne_travail'] if sommes['somme_duree_moyenne_travail'] is not None else 0
    somme_logement_des_travailleurs=sommes['somme_logement_des_travailleurs'] if sommes['somme_logement_des_travailleurs'] is not None else 0
    somme_approvionnement_eau_potable=sommes['somme_approvionnement_eau_potable'] if sommes['somme_approvionnement_eau_potable'] is not None else 0
    somme_nombre_acticivite_engagement=sommes['somme_nombre_acticivite_engagement'] if sommes['somme_nombre_acticivite_engagement'] is not None else 0
    somme_nombre_activites=sommes['somme_nombre_activites'] if sommes['somme_nombre_activites'] is not None else 0
    somme_induction_sur_site=sommes['somme_induction_sur_site'] if sommes['somme_induction_sur_site'] is not None else 0
    somme_exercice_urgence=sommes['somme_exercice_urgence'] if sommes['somme_exercice_urgence'] is not None else 0
    somme_toolbox=sommes['somme_toolbox'] if sommes['somme_toolbox'] is not None else 0
    somme_formation_specifique=sommes['somme_formation_specifique'] if sommes['somme_formation_specifique'] is not None else 0
    somme_starter=sommes['somme_starter'] if sommes['somme_starter'] is not None else 0
    somme_nombre_outil_hsses=sommes['somme_nombre_outil_hsses'] if sommes['somme_nombre_outil_hsses'] is not None else 0
    somme_nombre_inspection_hsses=sommes['somme_nombre_inspection_hsses'] if sommes['somme_nombre_inspection_hsses'] is not None else 0
    
    somme_totale = somme_homme + somme_femme + somme_effectif_total_sur_site + somme_heure_travailler + somme_fatalite + somme_accident + somme_poste_adapte + somme_soins_medicaux + somme_premier_secours + somme_presque_accident + somme_dommage_materiel + somme_heure_perdue + somme_km_parcouru + somme_nombre_incident + somme_nombre_acceleration_brusque + somme_nombre_depassement + somme_nombre_freinage_brusque + somme_nombre_de_malades + somme_violation_des_regles + somme_nombre_de_deversement + somme_volume_de_deversement + somme_surface_impactee + somme_nombre_inspection + somme_zones_de_dechets + somme_zones_de_stockage + somme_dechets_inerte + somme_dechets_organique + somme_dechets_plastique + somme_dechets_hydrocarbure + somme_dechets_d3e + somme_eaux_usees + somme_consommation_eau_extraite + somme_consommation_de_carburant + somme_consommation_electricite + somme_valeur_limite_seuil + somme_x_sur_site + somme_x_aux_racepteurs + somme_x_source_emission + somme_x_qualite_de_air + somme_x_sante + somme_x_securite + somme_x_environnement + somme_x_social + somme_aucun_incident_social + somme_nombre_de_travailleurs_migrants + somme_nombre_de_travailleurs_locaux + somme_pourcentage_main_oeuvre + somme_duree_moyenne_travail + somme_logement_des_travailleurs + somme_approvionnement_eau_potable + somme_nombre_acticivite_engagement + somme_nombre_activites + somme_induction_sur_site + somme_exercice_urgence + somme_toolbox + somme_formation_specifique + somme_starter + somme_nombre_outil_hsses + somme_nombre_inspection_hsses

    
    return somme_homme, somme_femme, somme_effectif_total_sur_site,somme_heure_travailler,somme_fatalite,somme_accident,somme_poste_adapte,somme_soins_medicaux,somme_premier_secours,somme_presque_accident,somme_dommage_materiel,somme_heure_perdue,somme_km_parcouru,somme_nombre_incident,somme_nombre_acceleration_brusque,somme_nombre_depassement,somme_nombre_freinage_brusque,somme_nombre_de_malades,somme_violation_des_regles,somme_nombre_de_deversement,somme_volume_de_deversement,somme_surface_impactee,somme_nombre_inspection,somme_zones_de_dechets,somme_zones_de_stockage,somme_dechets_inerte,somme_dechets_organique,somme_dechets_plastique,somme_dechets_hydrocarbure,somme_dechets_d3e,somme_eaux_usees,somme_consommation_eau_extraite,somme_consommation_de_carburant,somme_consommation_electricite,somme_valeur_limite_seuil,somme_x_sur_site,somme_x_aux_racepteurs,somme_x_source_emission,somme_x_qualite_de_air,somme_x_sante,somme_x_securite,somme_x_environnement,somme_x_social,somme_aucun_incident_social,somme_nombre_de_travailleurs_migrants,somme_nombre_de_travailleurs_locaux,somme_pourcentage_main_oeuvre,somme_duree_moyenne_travail,somme_logement_des_travailleurs,somme_approvionnement_eau_potable,somme_nombre_acticivite_engagement,somme_nombre_activites,somme_induction_sur_site,somme_exercice_urgence,somme_toolbox,somme_formation_specifique,somme_starter,somme_nombre_outil_hsses,somme_nombre_inspection_hsses,somme_totale



def somme_station_service():
    sommes = KPI_station_service.objects.aggregate(
        somme_homme=Sum('homme'),
        somme_femme=Sum('femme'),
        somme_effectif_total_sur_site=Sum('effectif_total_sur_site'),
        somme_heure_travailler=Sum('heure_travailler'),
        somme_fatalite=Sum('fatalite'),
        somme_accident=Sum('accident'),
        somme_poste_adapte=Sum('poste_adapte'),
        somme_soins_medicaux=Sum('soins_medicaux'),
        somme_premier_secours=Sum('premier_secours'),
        somme_presque_accident=Sum('presque_accident'),
        somme_dommage_materiel=Sum('dommage_materiel'),
        somme_heure_perdue=Sum('heure_perdue'),
        somme_km_parcouru=Sum('km_parcouru'),
        somme_nombre_incident=Sum('nombre_incident'),
        somme_nombre_acceleration_brusque=Sum('nombre_acceleration_brusque'),
        somme_nombre_freinage_brusque=Sum('nombre_freinage_brusque'),
        somme_nombre_depassement=Sum('nombre_depassement'),
        
        somme_nombre_de_malades=Sum('nombre_de_malades'),
        somme_violation_des_regles=Sum('violation_des_regles'),
        somme_nombre_de_deversement=Sum('nombre_de_deversement'),
        somme_volume_de_deversement=Sum('volume_de_deversement'),
        somme_surface_impactee=Sum('surface_impactee'),
        somme_nombre_inspection=Sum('nombre_inspection'),
        somme_zones_de_dechets=Sum('zones_de_dechets'),
        somme_zones_de_stockage=Sum('zones_de_stockage'),
        somme_dechets_inerte=Sum('dechets_inerte'),
        somme_dechets_organique=Sum('dechets_organique'),
        somme_dechets_plastique=Sum('dechets_plastique'),
        somme_dechets_hydrocarbure=Sum('dechets_hydrocarbure'),
        somme_dechets_d3e=Sum('dechets_d3e'),
        somme_eaux_usees=Sum('eaux_usees'),
        somme_consommation_eau_extraite=Sum('consommation_eau_extraite'),
        somme_consommation_de_carburant=Sum('consommation_de_carburant'),
        somme_consommation_electricite=Sum('consommation_electricite'),
        somme_valeur_limite_seuil=Sum('valeur_limite_seuil'),
        somme_x_sur_site=Sum('x_sur_site'),
        somme_x_aux_racepteurs=Sum('x_aux_racepteurs'),
        somme_x_source_emission=Sum('x_source_emission'),
        somme_x_qualite_de_air=Sum('x_qualite_de_air'),
        somme_x_sante=Sum('x_sante'),
        somme_x_securite=Sum('x_securite'),
        somme_x_environnement=Sum('x_environnement'),
        somme_x_social=Sum('x_social'),
        somme_aucun_incident_social=Sum('aucun_incident_social'),
        somme_nombre_de_travailleurs_migrants=Sum('nombre_de_travailleurs_migrants'),
        somme_nombre_de_travailleurs_locaux=Sum('nombre_de_travailleurs_locaux'),
        somme_pourcentage_main_oeuvre=Sum('pourcentage_main_oeuvre'),
        somme_duree_moyenne_travail=Sum('duree_moyenne_travail'),
        somme_logement_des_travailleurs=Sum('logement_des_travailleurs'),
        somme_approvionnement_eau_potable=Sum('approvionnement_eau_potable'),
        somme_nombre_acticivite_engagement=Sum('nombre_acticivite_engagement'),
        somme_nombre_activites=Sum('nombre_activites'),
        somme_induction_sur_site=Sum('induction_sur_site'),
        somme_exercice_urgence=Sum('exercice_urgence'),
        somme_toolbox=Sum('toolbox'),
        somme_formation_specifique=Sum('formation_specifique'),
        somme_starter=Sum('starter'),
        somme_nombre_outil_hsses=Sum('nombre_outil_hsses'),
        somme_nombre_inspection_hsses=Sum('nombre_inspection_hsses'),
        
    )
    
    somme_homme = sommes['somme_homme'] if sommes['somme_homme'] is not None else 0
    somme_femme = sommes['somme_femme'] if sommes['somme_femme'] is not None else 0
    somme_effectif_total_sur_site = sommes['somme_effectif_total_sur_site'] if sommes['somme_effectif_total_sur_site'] is not None else 1
    somme_heure_travailler=sommes['somme_heure_travailler']if sommes['somme_heure_travailler'] is not None else 0
    somme_fatalite=sommes['somme_fatalite']if sommes['somme_fatalite'] is not None else 0
    somme_accident=sommes['somme_accident']if sommes['somme_accident'] is not None else 0
    somme_poste_adapte=sommes['somme_poste_adapte']if sommes['somme_poste_adapte'] is not None else 0
    somme_soins_medicaux=sommes['somme_soins_medicaux']if sommes['somme_soins_medicaux'] is not None else 0
    somme_premier_secours=sommes['somme_premier_secours']if sommes['somme_premier_secours'] is not None else 0
    somme_presque_accident=sommes['somme_presque_accident']if sommes['somme_presque_accident'] is not None else 0
    somme_dommage_materiel=sommes['somme_dommage_materiel']if sommes['somme_dommage_materiel'] is not None else 0
    somme_heure_perdue=sommes['somme_heure_perdue']if sommes['somme_heure_perdue'] is not None else 0
    somme_km_parcouru=sommes['somme_km_parcouru']if sommes['somme_km_parcouru'] is not None else 0
    somme_nombre_incident=sommes['somme_nombre_incident']if sommes['somme_nombre_incident'] is not None else 0
    somme_nombre_acceleration_brusque=sommes['somme_nombre_acceleration_brusque']if sommes['somme_nombre_acceleration_brusque'] is not None else 0
    somme_nombre_freinage_brusque=sommes['somme_nombre_freinage_brusque']if sommes['somme_nombre_freinage_brusque'] is not None else 0
    somme_nombre_depassement=sommes['somme_nombre_depassement']if sommes['somme_nombre_depassement'] is not None else 0
    
    somme_nombre_de_malades=sommes['somme_nombre_de_malades'] if sommes['somme_nombre_de_malades'] is not None else 0
    somme_violation_des_regles=sommes['somme_violation_des_regles'] if sommes['somme_violation_des_regles'] is not None else 0
    somme_nombre_de_deversement=sommes['somme_nombre_de_deversement'] if sommes['somme_nombre_de_deversement'] is not None else 0
    somme_volume_de_deversement=sommes['somme_volume_de_deversement'] if sommes['somme_volume_de_deversement'] is not None else 0
    somme_surface_impactee=sommes['somme_surface_impactee'] if sommes['somme_surface_impactee'] is not None else 0
    somme_nombre_inspection=sommes['somme_nombre_inspection'] if sommes['somme_nombre_inspection'] is not None else 0
    somme_zones_de_dechets=sommes['somme_zones_de_dechets'] if sommes['somme_zones_de_dechets'] is not None else 0
    somme_zones_de_stockage=sommes['somme_zones_de_stockage'] if sommes['somme_zones_de_stockage'] is not None else 0
    somme_dechets_inerte=sommes['somme_dechets_inerte'] if sommes['somme_dechets_inerte'] is not None else 0
    somme_dechets_organique=sommes['somme_dechets_organique'] if sommes['somme_dechets_organique'] is not None else 0
    somme_dechets_plastique=sommes['somme_dechets_plastique'] if sommes['somme_dechets_plastique'] is not None else 0
    somme_dechets_hydrocarbure=sommes['somme_dechets_hydrocarbure'] if sommes['somme_dechets_hydrocarbure'] is not None else 0
    somme_dechets_d3e=sommes['somme_dechets_d3e'] if sommes['somme_dechets_d3e'] is not None else 0
    somme_eaux_usees=sommes['somme_eaux_usees'] if sommes['somme_eaux_usees'] is not None else 0
    somme_consommation_eau_extraite=sommes['somme_consommation_eau_extraite'] if sommes['somme_consommation_eau_extraite'] is not None else 0
    somme_consommation_de_carburant=sommes['somme_consommation_de_carburant'] if sommes['somme_consommation_de_carburant'] is not None else 0
    somme_consommation_electricite=sommes['somme_consommation_electricite'] if sommes['somme_consommation_electricite'] is not None else 0
    somme_valeur_limite_seuil=sommes['somme_valeur_limite_seuil'] if sommes['somme_valeur_limite_seuil'] is not None else 0
    somme_x_sur_site=sommes['somme_x_sur_site'] if sommes['somme_x_sur_site'] is not None else 0
    somme_x_aux_racepteurs=sommes['somme_x_aux_racepteurs'] if sommes['somme_x_aux_racepteurs'] is not None else 0
    somme_x_source_emission=sommes['somme_x_source_emission'] if sommes['somme_x_source_emission'] is not None else 0
    somme_x_qualite_de_air=sommes['somme_x_qualite_de_air'] if sommes['somme_x_qualite_de_air'] is not None else 0
    somme_x_sante=sommes['somme_x_sante'] if sommes['somme_x_sante'] is not None else 0
    somme_x_securite=sommes['somme_x_securite'] if sommes['somme_x_securite'] is not None else 0
    somme_x_environnement=sommes['somme_x_environnement'] if sommes['somme_x_environnement'] is not None else 0
    somme_x_social=sommes['somme_x_social'] if sommes['somme_x_social'] is not None else 0
    somme_aucun_incident_social=sommes['somme_aucun_incident_social'] if sommes['somme_aucun_incident_social'] is not None else 0
    somme_nombre_de_travailleurs_migrants=sommes['somme_nombre_de_travailleurs_migrants'] if sommes['somme_nombre_de_travailleurs_migrants'] is not None else 0
    somme_nombre_de_travailleurs_locaux=sommes['somme_nombre_de_travailleurs_locaux'] if sommes['somme_nombre_de_travailleurs_locaux'] is not None else 0
    somme_pourcentage_main_oeuvre=sommes['somme_pourcentage_main_oeuvre'] if sommes['somme_pourcentage_main_oeuvre'] is not None else 0
    somme_duree_moyenne_travail=sommes['somme_duree_moyenne_travail'] if sommes['somme_duree_moyenne_travail'] is not None else 0
    somme_logement_des_travailleurs=sommes['somme_logement_des_travailleurs'] if sommes['somme_logement_des_travailleurs'] is not None else 0
    somme_approvionnement_eau_potable=sommes['somme_approvionnement_eau_potable'] if sommes['somme_approvionnement_eau_potable'] is not None else 0
    somme_nombre_acticivite_engagement=sommes['somme_nombre_acticivite_engagement'] if sommes['somme_nombre_acticivite_engagement'] is not None else 0
    somme_nombre_activites=sommes['somme_nombre_activites'] if sommes['somme_nombre_activites'] is not None else 0
    somme_induction_sur_site=sommes['somme_induction_sur_site'] if sommes['somme_induction_sur_site'] is not None else 0
    somme_exercice_urgence=sommes['somme_exercice_urgence'] if sommes['somme_exercice_urgence'] is not None else 0
    somme_toolbox=sommes['somme_toolbox'] if sommes['somme_toolbox'] is not None else 0
    somme_formation_specifique=sommes['somme_formation_specifique'] if sommes['somme_formation_specifique'] is not None else 0
    somme_starter=sommes['somme_starter'] if sommes['somme_starter'] is not None else 0
    somme_nombre_outil_hsses=sommes['somme_nombre_outil_hsses'] if sommes['somme_nombre_outil_hsses'] is not None else 0
    somme_nombre_inspection_hsses=sommes['somme_nombre_inspection_hsses'] if sommes['somme_nombre_inspection_hsses'] is not None else 0
    
    somme_totale = somme_homme + somme_femme + somme_effectif_total_sur_site + somme_heure_travailler + somme_fatalite + somme_accident + somme_poste_adapte + somme_soins_medicaux + somme_premier_secours + somme_presque_accident + somme_dommage_materiel + somme_heure_perdue + somme_km_parcouru + somme_nombre_incident + somme_nombre_acceleration_brusque + somme_nombre_depassement + somme_nombre_freinage_brusque + somme_nombre_de_malades + somme_violation_des_regles + somme_nombre_de_deversement + somme_volume_de_deversement + somme_surface_impactee + somme_nombre_inspection + somme_zones_de_dechets + somme_zones_de_stockage + somme_dechets_inerte + somme_dechets_organique + somme_dechets_plastique + somme_dechets_hydrocarbure + somme_dechets_d3e + somme_eaux_usees + somme_consommation_eau_extraite + somme_consommation_de_carburant + somme_consommation_electricite + somme_valeur_limite_seuil + somme_x_sur_site + somme_x_aux_racepteurs + somme_x_source_emission + somme_x_qualite_de_air + somme_x_sante + somme_x_securite + somme_x_environnement + somme_x_social + somme_aucun_incident_social + somme_nombre_de_travailleurs_migrants + somme_nombre_de_travailleurs_locaux + somme_pourcentage_main_oeuvre + somme_duree_moyenne_travail + somme_logement_des_travailleurs + somme_approvionnement_eau_potable + somme_nombre_acticivite_engagement + somme_nombre_activites + somme_induction_sur_site + somme_exercice_urgence + somme_toolbox + somme_formation_specifique + somme_starter + somme_nombre_outil_hsses + somme_nombre_inspection_hsses

    
    return somme_homme, somme_femme, somme_effectif_total_sur_site,somme_heure_travailler,somme_fatalite,somme_accident,somme_poste_adapte,somme_soins_medicaux,somme_premier_secours,somme_presque_accident,somme_dommage_materiel,somme_heure_perdue,somme_km_parcouru,somme_nombre_incident,somme_nombre_acceleration_brusque,somme_nombre_depassement,somme_nombre_freinage_brusque,somme_nombre_de_malades,somme_violation_des_regles,somme_nombre_de_deversement,somme_volume_de_deversement,somme_surface_impactee,somme_nombre_inspection,somme_zones_de_dechets,somme_zones_de_stockage,somme_dechets_inerte,somme_dechets_organique,somme_dechets_plastique,somme_dechets_hydrocarbure,somme_dechets_d3e,somme_eaux_usees,somme_consommation_eau_extraite,somme_consommation_de_carburant,somme_consommation_electricite,somme_valeur_limite_seuil,somme_x_sur_site,somme_x_aux_racepteurs,somme_x_source_emission,somme_x_qualite_de_air,somme_x_sante,somme_x_securite,somme_x_environnement,somme_x_social,somme_aucun_incident_social,somme_nombre_de_travailleurs_migrants,somme_nombre_de_travailleurs_locaux,somme_pourcentage_main_oeuvre,somme_duree_moyenne_travail,somme_logement_des_travailleurs,somme_approvionnement_eau_potable,somme_nombre_acticivite_engagement,somme_nombre_activites,somme_induction_sur_site,somme_exercice_urgence,somme_toolbox,somme_formation_specifique,somme_starter,somme_nombre_outil_hsses,somme_nombre_inspection_hsses,somme_totale

    

def somme_transporteur():
    sommes = KPI_transporteur.objects.aggregate(
        somme_homme=Sum('homme'),
        somme_femme=Sum('femme'),
        somme_effectif_total_sur_site=Sum('effectif_total_sur_site'),
        somme_heure_travailler=Sum('heure_travailler'),
        somme_fatalite=Sum('fatalite'),
        somme_accident=Sum('accident'),
        somme_poste_adapte=Sum('poste_adapte'),
        somme_soins_medicaux=Sum('soins_medicaux'),
        somme_premier_secours=Sum('premier_secours'),
        somme_presque_accident=Sum('presque_accident'),
        somme_dommage_materiel=Sum('dommage_materiel'),
        somme_heure_perdue=Sum('heure_perdue'),
        somme_km_parcouru=Sum('km_parcouru'),
        somme_nombre_incident=Sum('nombre_incident'),
        somme_nombre_acceleration_brusque=Sum('nombre_acceleration_brusque'),
        somme_nombre_freinage_brusque=Sum('nombre_freinage_brusque'),
        somme_nombre_depassement=Sum('nombre_depassement'),
        
        somme_nombre_de_malades=Sum('nombre_de_malades'),
        somme_violation_des_regles=Sum('violation_des_regles'),
        somme_nombre_de_deversement=Sum('nombre_de_deversement'),
        somme_volume_de_deversement=Sum('volume_de_deversement'),
        somme_surface_impactee=Sum('surface_impactee'),
        somme_nombre_inspection=Sum('nombre_inspection'),
        somme_zones_de_dechets=Sum('zones_de_dechets'),
        somme_zones_de_stockage=Sum('zones_de_stockage'),
        somme_dechets_inerte=Sum('dechets_inerte'),
        somme_dechets_organique=Sum('dechets_organique'),
        somme_dechets_plastique=Sum('dechets_plastique'),
        somme_dechets_hydrocarbure=Sum('dechets_hydrocarbure'),
        somme_dechets_d3e=Sum('dechets_d3e'),
        somme_eaux_usees=Sum('eaux_usees'),
        somme_consommation_eau_extraite=Sum('consommation_eau_extraite'),
        somme_consommation_de_carburant=Sum('consommation_de_carburant'),
        somme_consommation_electricite=Sum('consommation_electricite'),
        somme_valeur_limite_seuil=Sum('valeur_limite_seuil'),
        somme_x_sur_site=Sum('x_sur_site'),
        somme_x_aux_racepteurs=Sum('x_aux_racepteurs'),
        somme_x_source_emission=Sum('x_source_emission'),
        somme_x_qualite_de_air=Sum('x_qualite_de_air'),
        somme_x_sante=Sum('x_sante'),
        somme_x_securite=Sum('x_securite'),
        somme_x_environnement=Sum('x_environnement'),
        somme_x_social=Sum('x_social'),
        somme_aucun_incident_social=Sum('aucun_incident_social'),
        somme_nombre_de_travailleurs_migrants=Sum('nombre_de_travailleurs_migrants'),
        somme_nombre_de_travailleurs_locaux=Sum('nombre_de_travailleurs_locaux'),
        somme_pourcentage_main_oeuvre=Sum('pourcentage_main_oeuvre'),
        somme_duree_moyenne_travail=Sum('duree_moyenne_travail'),
        somme_logement_des_travailleurs=Sum('logement_des_travailleurs'),
        somme_approvionnement_eau_potable=Sum('approvionnement_eau_potable'),
        somme_nombre_acticivite_engagement=Sum('nombre_acticivite_engagement'),
        somme_nombre_activites=Sum('nombre_activites'),
        somme_induction_sur_site=Sum('induction_sur_site'),
        somme_exercice_urgence=Sum('exercice_urgence'),
        somme_toolbox=Sum('toolbox'),
        somme_formation_specifique=Sum('formation_specifique'),
        somme_starter=Sum('starter'),
        somme_nombre_outil_hsses=Sum('nombre_outil_hsses'),
        somme_nombre_inspection_hsses=Sum('nombre_inspection_hsses'),
        
    )
    
    somme_homme = sommes['somme_homme'] if sommes['somme_homme'] is not None else 0
    somme_femme = sommes['somme_femme'] if sommes['somme_femme'] is not None else 0
    somme_effectif_total_sur_site = sommes['somme_effectif_total_sur_site'] if sommes['somme_effectif_total_sur_site'] is not None else 1
    somme_heure_travailler=sommes['somme_heure_travailler']if sommes['somme_heure_travailler'] is not None else 0
    somme_fatalite=sommes['somme_fatalite']if sommes['somme_fatalite'] is not None else 0
    somme_accident=sommes['somme_accident']if sommes['somme_accident'] is not None else 0
    somme_poste_adapte=sommes['somme_poste_adapte']if sommes['somme_poste_adapte'] is not None else 0
    somme_soins_medicaux=sommes['somme_soins_medicaux']if sommes['somme_soins_medicaux'] is not None else 0
    somme_premier_secours=sommes['somme_premier_secours']if sommes['somme_premier_secours'] is not None else 0
    somme_presque_accident=sommes['somme_presque_accident']if sommes['somme_presque_accident'] is not None else 0
    somme_dommage_materiel=sommes['somme_dommage_materiel']if sommes['somme_dommage_materiel'] is not None else 0
    somme_heure_perdue=sommes['somme_heure_perdue']if sommes['somme_heure_perdue'] is not None else 0
    somme_km_parcouru=sommes['somme_km_parcouru']if sommes['somme_km_parcouru'] is not None else 0
    somme_nombre_incident=sommes['somme_nombre_incident']if sommes['somme_nombre_incident'] is not None else 0
    somme_nombre_acceleration_brusque=sommes['somme_nombre_acceleration_brusque']if sommes['somme_nombre_acceleration_brusque'] is not None else 0
    somme_nombre_freinage_brusque=sommes['somme_nombre_freinage_brusque']if sommes['somme_nombre_freinage_brusque'] is not None else 0
    somme_nombre_depassement=sommes['somme_nombre_depassement']if sommes['somme_nombre_depassement'] is not None else 0
    
    somme_nombre_de_malades=sommes['somme_nombre_de_malades'] if sommes['somme_nombre_de_malades'] is not None else 0
    somme_violation_des_regles=sommes['somme_violation_des_regles'] if sommes['somme_violation_des_regles'] is not None else 0
    somme_nombre_de_deversement=sommes['somme_nombre_de_deversement'] if sommes['somme_nombre_de_deversement'] is not None else 0
    somme_volume_de_deversement=sommes['somme_volume_de_deversement'] if sommes['somme_volume_de_deversement'] is not None else 0
    somme_surface_impactee=sommes['somme_surface_impactee'] if sommes['somme_surface_impactee'] is not None else 0
    somme_nombre_inspection=sommes['somme_nombre_inspection'] if sommes['somme_nombre_inspection'] is not None else 0
    somme_zones_de_dechets=sommes['somme_zones_de_dechets'] if sommes['somme_zones_de_dechets'] is not None else 0
    somme_zones_de_stockage=sommes['somme_zones_de_stockage'] if sommes['somme_zones_de_stockage'] is not None else 0
    somme_dechets_inerte=sommes['somme_dechets_inerte'] if sommes['somme_dechets_inerte'] is not None else 0
    somme_dechets_organique=sommes['somme_dechets_organique'] if sommes['somme_dechets_organique'] is not None else 0
    somme_dechets_plastique=sommes['somme_dechets_plastique'] if sommes['somme_dechets_plastique'] is not None else 0
    somme_dechets_hydrocarbure=sommes['somme_dechets_hydrocarbure'] if sommes['somme_dechets_hydrocarbure'] is not None else 0
    somme_dechets_d3e=sommes['somme_dechets_d3e'] if sommes['somme_dechets_d3e'] is not None else 0
    somme_eaux_usees=sommes['somme_eaux_usees'] if sommes['somme_eaux_usees'] is not None else 0
    somme_consommation_eau_extraite=sommes['somme_consommation_eau_extraite'] if sommes['somme_consommation_eau_extraite'] is not None else 0
    somme_consommation_de_carburant=sommes['somme_consommation_de_carburant'] if sommes['somme_consommation_de_carburant'] is not None else 0
    somme_consommation_electricite=sommes['somme_consommation_electricite'] if sommes['somme_consommation_electricite'] is not None else 0
    somme_valeur_limite_seuil=sommes['somme_valeur_limite_seuil'] if sommes['somme_valeur_limite_seuil'] is not None else 0
    somme_x_sur_site=sommes['somme_x_sur_site'] if sommes['somme_x_sur_site'] is not None else 0
    somme_x_aux_racepteurs=sommes['somme_x_aux_racepteurs'] if sommes['somme_x_aux_racepteurs'] is not None else 0
    somme_x_source_emission=sommes['somme_x_source_emission'] if sommes['somme_x_source_emission'] is not None else 0
    somme_x_qualite_de_air=sommes['somme_x_qualite_de_air'] if sommes['somme_x_qualite_de_air'] is not None else 0
    somme_x_sante=sommes['somme_x_sante'] if sommes['somme_x_sante'] is not None else 0
    somme_x_securite=sommes['somme_x_securite'] if sommes['somme_x_securite'] is not None else 0
    somme_x_environnement=sommes['somme_x_environnement'] if sommes['somme_x_environnement'] is not None else 0
    somme_x_social=sommes['somme_x_social'] if sommes['somme_x_social'] is not None else 0
    somme_aucun_incident_social=sommes['somme_aucun_incident_social'] if sommes['somme_aucun_incident_social'] is not None else 0
    somme_nombre_de_travailleurs_migrants=sommes['somme_nombre_de_travailleurs_migrants'] if sommes['somme_nombre_de_travailleurs_migrants'] is not None else 0
    somme_nombre_de_travailleurs_locaux=sommes['somme_nombre_de_travailleurs_locaux'] if sommes['somme_nombre_de_travailleurs_locaux'] is not None else 0
    somme_pourcentage_main_oeuvre=sommes['somme_pourcentage_main_oeuvre'] if sommes['somme_pourcentage_main_oeuvre'] is not None else 0
    somme_duree_moyenne_travail=sommes['somme_duree_moyenne_travail'] if sommes['somme_duree_moyenne_travail'] is not None else 0
    somme_logement_des_travailleurs=sommes['somme_logement_des_travailleurs'] if sommes['somme_logement_des_travailleurs'] is not None else 0
    somme_approvionnement_eau_potable=sommes['somme_approvionnement_eau_potable'] if sommes['somme_approvionnement_eau_potable'] is not None else 0
    somme_nombre_acticivite_engagement=sommes['somme_nombre_acticivite_engagement'] if sommes['somme_nombre_acticivite_engagement'] is not None else 0
    somme_nombre_activites=sommes['somme_nombre_activites'] if sommes['somme_nombre_activites'] is not None else 0
    somme_induction_sur_site=sommes['somme_induction_sur_site'] if sommes['somme_induction_sur_site'] is not None else 0
    somme_exercice_urgence=sommes['somme_exercice_urgence'] if sommes['somme_exercice_urgence'] is not None else 0
    somme_toolbox=sommes['somme_toolbox'] if sommes['somme_toolbox'] is not None else 0
    somme_formation_specifique=sommes['somme_formation_specifique'] if sommes['somme_formation_specifique'] is not None else 0
    somme_starter=sommes['somme_starter'] if sommes['somme_starter'] is not None else 0
    somme_nombre_outil_hsses=sommes['somme_nombre_outil_hsses'] if sommes['somme_nombre_outil_hsses'] is not None else 0
    somme_nombre_inspection_hsses=sommes['somme_nombre_inspection_hsses'] if sommes['somme_nombre_inspection_hsses'] is not None else 0
    
    somme_totale = somme_homme + somme_femme + somme_effectif_total_sur_site + somme_heure_travailler + somme_fatalite + somme_accident + somme_poste_adapte + somme_soins_medicaux + somme_premier_secours + somme_presque_accident + somme_dommage_materiel + somme_heure_perdue + somme_km_parcouru + somme_nombre_incident + somme_nombre_acceleration_brusque + somme_nombre_depassement + somme_nombre_freinage_brusque + somme_nombre_de_malades + somme_violation_des_regles + somme_nombre_de_deversement + somme_volume_de_deversement + somme_surface_impactee + somme_nombre_inspection + somme_zones_de_dechets + somme_zones_de_stockage + somme_dechets_inerte + somme_dechets_organique + somme_dechets_plastique + somme_dechets_hydrocarbure + somme_dechets_d3e + somme_eaux_usees + somme_consommation_eau_extraite + somme_consommation_de_carburant + somme_consommation_electricite + somme_valeur_limite_seuil + somme_x_sur_site + somme_x_aux_racepteurs + somme_x_source_emission + somme_x_qualite_de_air + somme_x_sante + somme_x_securite + somme_x_environnement + somme_x_social + somme_aucun_incident_social + somme_nombre_de_travailleurs_migrants + somme_nombre_de_travailleurs_locaux + somme_pourcentage_main_oeuvre + somme_duree_moyenne_travail + somme_logement_des_travailleurs + somme_approvionnement_eau_potable + somme_nombre_acticivite_engagement + somme_nombre_activites + somme_induction_sur_site + somme_exercice_urgence + somme_toolbox + somme_formation_specifique + somme_starter + somme_nombre_outil_hsses + somme_nombre_inspection_hsses

    
    return somme_homme, somme_femme, somme_effectif_total_sur_site,somme_heure_travailler,somme_fatalite,somme_accident,somme_poste_adapte,somme_soins_medicaux,somme_premier_secours,somme_presque_accident,somme_dommage_materiel,somme_heure_perdue,somme_km_parcouru,somme_nombre_incident,somme_nombre_acceleration_brusque,somme_nombre_depassement,somme_nombre_freinage_brusque,somme_nombre_de_malades,somme_violation_des_regles,somme_nombre_de_deversement,somme_volume_de_deversement,somme_surface_impactee,somme_nombre_inspection,somme_zones_de_dechets,somme_zones_de_stockage,somme_dechets_inerte,somme_dechets_organique,somme_dechets_plastique,somme_dechets_hydrocarbure,somme_dechets_d3e,somme_eaux_usees,somme_consommation_eau_extraite,somme_consommation_de_carburant,somme_consommation_electricite,somme_valeur_limite_seuil,somme_x_sur_site,somme_x_aux_racepteurs,somme_x_source_emission,somme_x_qualite_de_air,somme_x_sante,somme_x_securite,somme_x_environnement,somme_x_social,somme_aucun_incident_social,somme_nombre_de_travailleurs_migrants,somme_nombre_de_travailleurs_locaux,somme_pourcentage_main_oeuvre,somme_duree_moyenne_travail,somme_logement_des_travailleurs,somme_approvionnement_eau_potable,somme_nombre_acticivite_engagement,somme_nombre_activites,somme_induction_sur_site,somme_exercice_urgence,somme_toolbox,somme_formation_specifique,somme_starter,somme_nombre_outil_hsses,somme_nombre_inspection_hsses,somme_totale

    
