
from datetime import date, datetime
from django.utils import timezone
from django.db import models

from django.db import models
from django.dispatch import receiver
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from app.gerer import generate_id

from django.core.validators import MaxValueValidator, MinValueValidator

import uuid

class KPI_jovena(models.Model):
    name = models.CharField(max_length=20, default="N/A")
    
    # PERFORMANCE SANTE
    homme = models.PositiveBigIntegerField(default=0)
    femme = models.PositiveBigIntegerField(default=0)
    effectif_total_sur_site = models.PositiveBigIntegerField(default=1)
    
    heure_travailler = models.PositiveBigIntegerField(default=0)
    
    fatalite = models.PositiveBigIntegerField(default=0)
    
    accident = models.PositiveBigIntegerField(default=0)
    poste_adapte = models.PositiveBigIntegerField(default=0)
    soins_medicaux = models.PositiveBigIntegerField(default=0)
    premier_secours = models.PositiveBigIntegerField(default=0)
    presque_accident = models.PositiveBigIntegerField(default=0)
    
    dommage_materiel = models.PositiveBigIntegerField(default=0)
    heure_perdue = models.PositiveBigIntegerField(default=0)
    
    # ACCIDENT DE CIRCULATION
    km_parcouru = models.PositiveBigIntegerField(default=0)
    nombre_incident = models.PositiveBigIntegerField(default=0)
    nombre_acceleration_brusque = models.PositiveBigIntegerField(default=0)
    nombre_freinage_brusque = models.PositiveBigIntegerField(default=0)
    nombre_depassement = models.PositiveBigIntegerField(default=0)
    
    #SURETE/ACHE DE MALVEILLANCE
    nombre_de_malades=models.PositiveBigIntegerField(default=0)
    violation_des_regles=models.PositiveBigIntegerField(default=0)
    
    #PERFORMANCE ENVIRONNEMENTALES
    nombre_de_deversement=models.PositiveBigIntegerField(default=0)
    volume_de_deversement=models.PositiveBigIntegerField(default=0)
    surface_impactee=models.PositiveBigIntegerField(default=0)
    nombre_inspection=models.PositiveBigIntegerField(default=0)
    zones_de_dechets=models.PositiveBigIntegerField(default=0)
    zones_de_stockage=models.PositiveBigIntegerField(default=0)
    
    #PRODUCTION DE DECHETS
    dechets_inerte=models.PositiveBigIntegerField(default=0)
    dechets_organique=models.PositiveBigIntegerField(default=0)
    dechets_plastique=models.PositiveBigIntegerField(default=0)
    dechets_hydrocarbure=models.PositiveBigIntegerField(default=0)
    dechets_d3e=models.PositiveBigIntegerField(default=0)
    eaux_usees=models.PositiveBigIntegerField(default=0)
    consommation_eau_extraite=models.PositiveBigIntegerField(default=0)
    consommation_de_carburant=models.PositiveBigIntegerField(default=0)
    consommation_electricite=models.PositiveBigIntegerField(default=0)
    
    #NOMBRE DE DEPASSEMENT DE BRUIT
    valeur_limite_seuil=models.PositiveBigIntegerField(default=0)
    x_sur_site=models.PositiveBigIntegerField(default=0)
    x_aux_racepteurs=models.PositiveBigIntegerField(default=0)
    
    #NOMBRE DE DEPASSEMENT DE BRUIT
    x_source_emission=models.PositiveBigIntegerField(default=0)
    x_qualite_de_air=models.PositiveBigIntegerField(default=0)
    
    #NOMBRE DE GRIEFS LIES
    x_sante=models.PositiveBigIntegerField(default=0)
    x_securite=models.PositiveBigIntegerField(default=0)
    x_environnement=models.PositiveBigIntegerField(default=0)
    x_social=models.PositiveBigIntegerField(default=0)
    
    #PERFORMANCE SOCIALE
    aucun_incident_social=models.PositiveBigIntegerField(default=0)
    nombre_de_travailleurs_migrants=models.PositiveBigIntegerField(default=0)
    nombre_de_travailleurs_locaux=models.PositiveBigIntegerField(default=0)
    pourcentage_main_oeuvre=models.PositiveBigIntegerField(default=0)
    duree_moyenne_travail=models.PositiveBigIntegerField(default=0)
    
    #NOMBRE D INSPECTION
    logement_des_travailleurs=models.PositiveBigIntegerField(default=0)
    approvionnement_eau_potable=models.PositiveBigIntegerField(default=0)
    nombre_acticivite_engagement=models.PositiveBigIntegerField(default=0)
    nombre_activites=models.PositiveBigIntegerField(default=0)
    
    #FORMATION DES TRAVAILLEURS HSE
    induction_sur_site=models.PositiveBigIntegerField(default=0)
    exercice_urgence=models.PositiveBigIntegerField(default=0)
    toolbox=models.PositiveBigIntegerField(default=0)
    formation_specifique=models.PositiveBigIntegerField(default=0)
    starter=models.PositiveBigIntegerField(default=0)
    nombre_outil_hsses=models.PositiveBigIntegerField(default=0)
    nombre_inspection_hsses=models.PositiveBigIntegerField(default=0)
 
    
    
    # TOTAL - CALCULE
    taux_frequence_incident = models.PositiveBigIntegerField(default=0)
    taux_gravite_incident = models.PositiveBigIntegerField(default=0)
    date = models.DateField(default=date.today)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "KPI Jovena"
        verbose_name_plural = "KPI Jovena"

class KPI_prestataire(models.Model):
    name = models.CharField(max_length=20, default="N/A")
    date = models.DateField(default=date.today)
    # PERFORMANCE SANTE
    homme = models.PositiveBigIntegerField(default=0)
    femme = models.PositiveBigIntegerField(default=0)
    effectif_total_sur_site = models.PositiveBigIntegerField(default=1)
    
    heure_travailler = models.PositiveBigIntegerField(default=0)
    
    fatalite = models.PositiveBigIntegerField(default=0)
    
    accident = models.PositiveBigIntegerField(default=0)
    poste_adapte = models.PositiveBigIntegerField(default=0)
    soins_medicaux = models.PositiveBigIntegerField(default=0)
    premier_secours = models.PositiveBigIntegerField(default=0)
    presque_accident = models.PositiveBigIntegerField(default=0)
    
    dommage_materiel = models.PositiveBigIntegerField(default=0)
    heure_perdue = models.PositiveBigIntegerField(default=0)
    
    # ACCIDENT DE CIRCULATION
    km_parcouru = models.PositiveBigIntegerField(default=0)
    nombre_incident = models.PositiveBigIntegerField(default=0)
    nombre_acceleration_brusque = models.PositiveBigIntegerField(default=0)
    nombre_freinage_brusque = models.PositiveBigIntegerField(default=0)
    nombre_depassement = models.PositiveBigIntegerField(default=0)
    
    #SURETE/ACHE DE MALVEILLANCE
    nombre_de_malades=models.PositiveBigIntegerField(default=0)
    violation_des_regles=models.PositiveBigIntegerField(default=0)
    
    #PERFORMANCE ENVIRONNEMENTALES
    nombre_de_deversement=models.PositiveBigIntegerField(default=0)
    volume_de_deversement=models.PositiveBigIntegerField(default=0)
    surface_impactee=models.PositiveBigIntegerField(default=0)
    nombre_inspection=models.PositiveBigIntegerField(default=0)
    zones_de_dechets=models.PositiveBigIntegerField(default=0)
    zones_de_stockage=models.PositiveBigIntegerField(default=0)
    
    #PRODUCTION DE DECHETS
    dechets_inerte=models.PositiveBigIntegerField(default=0)
    dechets_organique=models.PositiveBigIntegerField(default=0)
    dechets_plastique=models.PositiveBigIntegerField(default=0)
    dechets_hydrocarbure=models.PositiveBigIntegerField(default=0)
    dechets_d3e=models.PositiveBigIntegerField(default=0)
    eaux_usees=models.PositiveBigIntegerField(default=0)
    consommation_eau_extraite=models.PositiveBigIntegerField(default=0)
    consommation_de_carburant=models.PositiveBigIntegerField(default=0)
    consommation_electricite=models.PositiveBigIntegerField(default=0)
    
    #NOMBRE DE DEPASSEMENT DE BRUIT
    valeur_limite_seuil=models.PositiveBigIntegerField(default=0)
    x_sur_site=models.PositiveBigIntegerField(default=0)
    x_aux_racepteurs=models.PositiveBigIntegerField(default=0)
    
    #NOMBRE DE DEPASSEMENT DE BRUIT
    x_source_emission=models.PositiveBigIntegerField(default=0)
    x_qualite_de_air=models.PositiveBigIntegerField(default=0)
    
    #NOMBRE DE GRIEFS LIES
    x_sante=models.PositiveBigIntegerField(default=0)
    x_securite=models.PositiveBigIntegerField(default=0)
    x_environnement=models.PositiveBigIntegerField(default=0)
    x_social=models.PositiveBigIntegerField(default=0)
    
    #PERFORMANCE SOCIALE
    aucun_incident_social=models.PositiveBigIntegerField(default=0)
    nombre_de_travailleurs_migrants=models.PositiveBigIntegerField(default=0)
    nombre_de_travailleurs_locaux=models.PositiveBigIntegerField(default=0)
    pourcentage_main_oeuvre=models.PositiveBigIntegerField(default=0)
    duree_moyenne_travail=models.PositiveBigIntegerField(default=0)
    
    #NOMBRE D INSPECTION
    logement_des_travailleurs=models.PositiveBigIntegerField(default=0)
    approvionnement_eau_potable=models.PositiveBigIntegerField(default=0)
    nombre_acticivite_engagement=models.PositiveBigIntegerField(default=0)
    nombre_activites=models.PositiveBigIntegerField(default=0)
    
    #FORMATION DES TRAVAILLEURS HSE
    induction_sur_site=models.PositiveBigIntegerField(default=0)
    exercice_urgence=models.PositiveBigIntegerField(default=0)
    toolbox=models.PositiveBigIntegerField(default=0)
    formation_specifique=models.PositiveBigIntegerField(default=0)
    starter=models.PositiveBigIntegerField(default=0)
    nombre_outil_hsses=models.PositiveBigIntegerField(default=0)
    nombre_inspection_hsses=models.PositiveBigIntegerField(default=0)
    
    # TOTAL - CALCULE
    taux_frequence_incident = models.PositiveBigIntegerField(default=0)
    taux_gravite_incident = models.PositiveBigIntegerField(default=0)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "KPI Prestataire"
        verbose_name_plural = "KPI Prestataire"


class KPI_station_service(models.Model):
    name = models.CharField(max_length=20, default="N/A")
    
    # PERFORMANCE SANTE
    homme = models.PositiveBigIntegerField(default=0)
    femme = models.PositiveBigIntegerField(default=0)
    effectif_total_sur_site = models.PositiveBigIntegerField(default=1)
    
    heure_travailler = models.PositiveBigIntegerField(default=0)
    
    fatalite = models.PositiveBigIntegerField(default=0)
    
    accident = models.PositiveBigIntegerField(default=0)
    poste_adapte = models.PositiveBigIntegerField(default=0)
    soins_medicaux = models.PositiveBigIntegerField(default=0)
    premier_secours = models.PositiveBigIntegerField(default=0)
    presque_accident = models.PositiveBigIntegerField(default=0)
    
    dommage_materiel = models.PositiveBigIntegerField(default=0)
    heure_perdue = models.PositiveBigIntegerField(default=0)
    
    # ACCIDENT DE CIRCULATION
    km_parcouru = models.PositiveBigIntegerField(default=0)
    nombre_incident = models.PositiveBigIntegerField(default=0)
    nombre_acceleration_brusque = models.PositiveBigIntegerField(default=0)
    nombre_freinage_brusque = models.PositiveBigIntegerField(default=0)
    nombre_depassement = models.PositiveBigIntegerField(default=0)
    
    #SURETE/ACHE DE MALVEILLANCE
    nombre_de_malades=models.PositiveBigIntegerField(default=0)
    violation_des_regles=models.PositiveBigIntegerField(default=0)
    
    #PERFORMANCE ENVIRONNEMENTALES
    nombre_de_deversement=models.PositiveBigIntegerField(default=0)
    volume_de_deversement=models.PositiveBigIntegerField(default=0)
    surface_impactee=models.PositiveBigIntegerField(default=0)
    nombre_inspection=models.PositiveBigIntegerField(default=0)
    zones_de_dechets=models.PositiveBigIntegerField(default=0)
    zones_de_stockage=models.PositiveBigIntegerField(default=0)
    
    #PRODUCTION DE DECHETS
    dechets_inerte=models.PositiveBigIntegerField(default=0)
    dechets_organique=models.PositiveBigIntegerField(default=0)
    dechets_plastique=models.PositiveBigIntegerField(default=0)
    dechets_hydrocarbure=models.PositiveBigIntegerField(default=0)
    dechets_d3e=models.PositiveBigIntegerField(default=0)
    eaux_usees=models.PositiveBigIntegerField(default=0)
    consommation_eau_extraite=models.PositiveBigIntegerField(default=0)
    consommation_de_carburant=models.PositiveBigIntegerField(default=0)
    consommation_electricite=models.PositiveBigIntegerField(default=0)
    
    #NOMBRE DE DEPASSEMENT DE BRUIT
    valeur_limite_seuil=models.PositiveBigIntegerField(default=0)
    x_sur_site=models.PositiveBigIntegerField(default=0)
    x_aux_racepteurs=models.PositiveBigIntegerField(default=0)
    
    #NOMBRE DE DEPASSEMENT DE BRUIT
    x_source_emission=models.PositiveBigIntegerField(default=0)
    x_qualite_de_air=models.PositiveBigIntegerField(default=0)
    
    #NOMBRE DE GRIEFS LIES
    x_sante=models.PositiveBigIntegerField(default=0)
    x_securite=models.PositiveBigIntegerField(default=0)
    x_environnement=models.PositiveBigIntegerField(default=0)
    x_social=models.PositiveBigIntegerField(default=0)
    
    #PERFORMANCE SOCIALE
    aucun_incident_social=models.PositiveBigIntegerField(default=0)
    nombre_de_travailleurs_migrants=models.PositiveBigIntegerField(default=0)
    nombre_de_travailleurs_locaux=models.PositiveBigIntegerField(default=0)
    pourcentage_main_oeuvre=models.PositiveBigIntegerField(default=0)
    duree_moyenne_travail=models.PositiveBigIntegerField(default=0)
    
    #NOMBRE D INSPECTION
    logement_des_travailleurs=models.PositiveBigIntegerField(default=0)
    approvionnement_eau_potable=models.PositiveBigIntegerField(default=0)
    nombre_acticivite_engagement=models.PositiveBigIntegerField(default=0)
    nombre_activites=models.PositiveBigIntegerField(default=0)
    
    #FORMATION DES TRAVAILLEURS HSE
    induction_sur_site=models.PositiveBigIntegerField(default=0)
    exercice_urgence=models.PositiveBigIntegerField(default=0)
    toolbox=models.PositiveBigIntegerField(default=0)
    formation_specifique=models.PositiveBigIntegerField(default=0)
    starter=models.PositiveBigIntegerField(default=0)
    nombre_outil_hsses=models.PositiveBigIntegerField(default=0)
    nombre_inspection_hsses=models.PositiveBigIntegerField(default=0)
 
    
    
    # TOTAL - CALCULE
    taux_frequence_incident = models.PositiveBigIntegerField(default=0)
    taux_gravite_incident = models.PositiveBigIntegerField(default=0)
    date = models.DateField(default=date.today)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "KPI Station"
        verbose_name_plural = "KPI Station"


class KPI_transporteur(models.Model):
    name = models.CharField(max_length=20, default="N/A")
    
    # PERFORMANCE SANTE
    homme = models.PositiveBigIntegerField(default=0)
    femme = models.PositiveBigIntegerField(default=0)
    effectif_total_sur_site = models.PositiveBigIntegerField(default=1)
    
    heure_travailler = models.PositiveBigIntegerField(default=0)
    
    fatalite = models.PositiveBigIntegerField(default=0)
    
    accident = models.PositiveBigIntegerField(default=0)
    poste_adapte = models.PositiveBigIntegerField(default=0)
    soins_medicaux = models.PositiveBigIntegerField(default=0)
    premier_secours = models.PositiveBigIntegerField(default=0)
    presque_accident = models.PositiveBigIntegerField(default=0)
    
    dommage_materiel = models.PositiveBigIntegerField(default=0)
    heure_perdue = models.PositiveBigIntegerField(default=0)
    
    # ACCIDENT DE CIRCULATION
    km_parcouru = models.PositiveBigIntegerField(default=0)
    nombre_incident = models.PositiveBigIntegerField(default=0)
    nombre_acceleration_brusque = models.PositiveBigIntegerField(default=0)
    nombre_freinage_brusque = models.PositiveBigIntegerField(default=0)
    nombre_depassement = models.PositiveBigIntegerField(default=0)
    
    #SURETE/ACHE DE MALVEILLANCE
    nombre_de_malades=models.PositiveBigIntegerField(default=0)
    violation_des_regles=models.PositiveBigIntegerField(default=0)
    
    #PERFORMANCE ENVIRONNEMENTALES
    nombre_de_deversement=models.PositiveBigIntegerField(default=0)
    volume_de_deversement=models.PositiveBigIntegerField(default=0)
    surface_impactee=models.PositiveBigIntegerField(default=0)
    nombre_inspection=models.PositiveBigIntegerField(default=0)
    zones_de_dechets=models.PositiveBigIntegerField(default=0)
    zones_de_stockage=models.PositiveBigIntegerField(default=0)
    
    #PRODUCTION DE DECHETS
    dechets_inerte=models.PositiveBigIntegerField(default=0)
    dechets_organique=models.PositiveBigIntegerField(default=0)
    dechets_plastique=models.PositiveBigIntegerField(default=0)
    dechets_hydrocarbure=models.PositiveBigIntegerField(default=0)
    dechets_d3e=models.PositiveBigIntegerField(default=0)
    eaux_usees=models.PositiveBigIntegerField(default=0)
    consommation_eau_extraite=models.PositiveBigIntegerField(default=0)
    consommation_de_carburant=models.PositiveBigIntegerField(default=0)
    consommation_electricite=models.PositiveBigIntegerField(default=0)
    
    #NOMBRE DE DEPASSEMENT DE BRUIT
    valeur_limite_seuil=models.PositiveBigIntegerField(default=0)
    x_sur_site=models.PositiveBigIntegerField(default=0)
    x_aux_racepteurs=models.PositiveBigIntegerField(default=0)
    
    #NOMBRE DE DEPASSEMENT DE BRUIT
    x_source_emission=models.PositiveBigIntegerField(default=0)
    x_qualite_de_air=models.PositiveBigIntegerField(default=0)
    
    #NOMBRE DE GRIEFS LIES
    x_sante=models.PositiveBigIntegerField(default=0)
    x_securite=models.PositiveBigIntegerField(default=0)
    x_environnement=models.PositiveBigIntegerField(default=0)
    x_social=models.PositiveBigIntegerField(default=0)
    
    #PERFORMANCE SOCIALE
    aucun_incident_social=models.PositiveBigIntegerField(default=0)
    nombre_de_travailleurs_migrants=models.PositiveBigIntegerField(default=0)
    nombre_de_travailleurs_locaux=models.PositiveBigIntegerField(default=0)
    pourcentage_main_oeuvre=models.PositiveBigIntegerField(default=0)
    duree_moyenne_travail=models.PositiveBigIntegerField(default=0)
    
    #NOMBRE D INSPECTION
    logement_des_travailleurs=models.PositiveBigIntegerField(default=0)
    approvionnement_eau_potable=models.PositiveBigIntegerField(default=0)
    nombre_acticivite_engagement=models.PositiveBigIntegerField(default=0)
    nombre_activites=models.PositiveBigIntegerField(default=0)
    
    #FORMATION DES TRAVAILLEURS HSE
    induction_sur_site=models.PositiveBigIntegerField(default=0)
    exercice_urgence=models.PositiveBigIntegerField(default=0)
    toolbox=models.PositiveBigIntegerField(default=0)
    formation_specifique=models.PositiveBigIntegerField(default=0)
    starter=models.PositiveBigIntegerField(default=0)
    nombre_outil_hsses=models.PositiveBigIntegerField(default=0)
    nombre_inspection_hsses=models.PositiveBigIntegerField(default=0)
 
    # TOTAL - CALCULE
    taux_frequence_incident = models.PositiveBigIntegerField(default=0)
    taux_gravite_incident = models.PositiveBigIntegerField(default=0)
    date = models.DateField(default=date.today)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "KPI Transporteur"
        verbose_name_plural = "KPI Transporteur"

class UserProfile(models.Model ):
    choix_poste = (
        ('jovena', 'Jovena'),
        ('prestataire', 'Prestataire'),
        ('station_service', 'Station_service'),
        ('transporteur', 'Transporteur')
    )
    
    user = models.OneToOneField(User , on_delete=models.CASCADE)
    poste = models.CharField(max_length=50 , null=True , default=None, choices=choix_poste)
    id_poste = models.CharField(max_length=50, blank=True, null=True)
   
    def __str__(self):
        return self.user.username 
    
    def save(self, *args, **kwargs):
        if self.poste:
            
            if self.poste=="jovena":
                self.id_poste = "J-"+ str(generate_id()) 
                
            elif self.poste=="prestataire":
                self.id_poste = "P-"+ str(generate_id()) 
                
            elif self.poste=="transporteur":
                self.id_poste = "T-"+ str(generate_id()) 
                
            else:
                self.id_poste = "S-" + str(generate_id()) 
        else:
             self.id_poste = ""  
                    
        super(UserProfile, self).save(*args, **kwargs)     
    
@receiver(post_save , sender= User)
def create_user_profile(sender , instance , created , **kwargs):
     if created :
         UserProfile.objects.create(user = instance )
    

class document_jov(models.Model):
    info_jov = models.TextField()
  
    def __str__(self):
        return self.info_jov 
    
    class Meta:
        verbose_name = "Document Jovena"
        verbose_name_plural = "Documents Jovena"
    
class document_prest(models.Model):
    info_prest = models.TextField()
    
    def __str__(self):
        return self.info_prest 
    
    class Meta:
        verbose_name = "Document Prestataire"
        verbose_name_plural = "Documents Prestataire"
    
class document_stat(models.Model):
    info_stat = models.TextField()
    
    def __str__(self):
        return self.info_stat
    
    class Meta:
        verbose_name = "Document Station"
        verbose_name_plural = "Documents Station"
    
class document_trans(models.Model):
    info_trans = models.TextField()
    
    def __str__(self):
        return self.info_trans
    
    class Meta:
        verbose_name = "Document Transporteur"
        verbose_name_plural = "Documents Transporteur"
    
#crud
class Checklist_stat(models.Model):
    user_profile = models.CharField(max_length=200, default="N/A")
    
    num_reclamation         = models.IntegerField(primary_key=True)
    panne_annoncee          = models.CharField(max_length=200, default="N/A")
    site                    = models.CharField(max_length=200, default="N/A")
    client                  = models.CharField(max_length=200, default="N/A")
    localite                = models.CharField(max_length=200, default="N/A")
    entreprise_intervenante = models.CharField(max_length=200, default="N/A")
    categorie_reclamation   = models.CharField(max_length=200, default="N/A")
    date_reclamation        = models.DateField(auto_now_add=True)
    echeance                = models.DateField()
    
    date_diagnostic         = models.DateTimeField(auto_now_add=True)
    interlocuteur           = models.CharField(max_length=200, default="N/A")
    fonction                = models.CharField(max_length=200, default="N/A")
    panne_reel              = models.CharField(max_length=200, default="N/A")
    
    permis_specifique       = models.BooleanField(default=False)
    information_personnel   = models.BooleanField(default=False)
    port_EPI                = models.BooleanField(default=True)
    balisage_perimetre      = models.BooleanField(default=False)
    extincteur_adapte       = models.BooleanField(default=False)
    interdiction_de_fumer   = models.BooleanField(default=False)
    
    livraison_carburant     = models.DateTimeField(blank=True , null=True)
    presence_zone           = models.CharField(max_length=200, default="N/A")
    autre_travaux           = models.CharField(max_length=200, default="N/A")
    
    
    travail_chaud           = models.BooleanField(default=False)
    percage_moulage_decoupage = models.BooleanField(default= False)
    chauffage_soudage       = models.BooleanField(default= False)
    grenaillage_sablage     = models.BooleanField(default= False)
    utilisation_equipement  = models.BooleanField(default= False)
    vidange_degazage        = models.BooleanField(default= False) 
    travaux_demolition      = models.BooleanField(default= False)
    travail_espace          = models.BooleanField(default = False)
    deplacement_site        = models.BooleanField(default = False)
    manutention_levage      = models.BooleanField(default = False)
    travail_hauteur         = models.BooleanField(default= False)
    travail_tuyauterie      = models.BooleanField(default = False)
    fouille_mannuelle       = models.BooleanField(default = False)
    travaux_excavation      = models.BooleanField(default = False)
    travail_equipement      = models.BooleanField(default = False)
    travail_engin           = models.BooleanField(default = False)
    operation_piste         = models.BooleanField(default = False)
    travaux_bruyant         = models.BooleanField(default = False)
    autre_nature            = models.CharField(max_length=100 , blank=True)
    
    
    emission_gaz            = models.BooleanField(default=False)
    incendie                = models.BooleanField(default=False)
    explosion               = models.BooleanField(default=False)
    projection_etincelle    = models.BooleanField(default=False)
    intoxication            = models.BooleanField(default=False)
    asphyxie                = models.BooleanField(default=False)
    brulure                 = models.BooleanField(default=False)
    blessure                = models.BooleanField(default=False)
    autre_lesion            = models.BooleanField(default=False)
    chute_plain_pied        = models.BooleanField(default=False)
    chute_objet             = models.BooleanField(default=False)
    chute_hauteur           = models.BooleanField(default=False)
    incident_reseau         = models.BooleanField(default=False)
    epandage                = models.BooleanField(default=False)
    eboulement              = models.BooleanField(default=False)
    electrocution           = models.BooleanField(default=False)
    incident_cable          = models.BooleanField(default=False)
    accident_circulation    = models.BooleanField(default=False)
    autre_lesion            = models.CharField(max_length=200, default="N/A")
    
    # choix = models.CharField(max_length=200, choices=(
    #     ('oui','OUI'),
    #     ('non','NON'),
    # ))
    
    # A la charge de la station service
    
    charge_station_service = models.CharField(max_length=10, default='N/A')
    arret_distribution_total = models.CharField(max_length=10, default='N/A')
    
    fermeture_station = models.BooleanField(default=False)
    arret_activite = models.CharField(max_length=200, default="N/A")
    
    # A la charge de la / les entreprise(s) extérieure(s)
    
    
    test_gaz = models.BooleanField(default=False)
    arret_travaux_depotage = models.BooleanField(default=False)
    arret_autre_travaux = models.BooleanField(default=False)
    extincteur_adapte2 = models.BooleanField(default=False)
    mise_terre = models.BooleanField(default=False)
    appareil_respiratoire = models.BooleanField(default=False)
    outillage = models.BooleanField(default=False)
    port_EPI_2 = models.BooleanField(default=False)
    harnai = models.BooleanField(default=False)
    echaffaudage = models.BooleanField(default=False)
    renseignement_reseaux_enterre = models.BooleanField(default=False)
    consignation_equipement = models.BooleanField(default=False)
    consignation_electrique = models.BooleanField(default=False)
    renseignement_reseau_aerien = models.BooleanField(default=False)
    aide_circulation = models.BooleanField(default=False)
    
    # B-6 VISAS
    # Entreprise Extérieur intervenant (y compris les sous-traitant)
    responsable_intervention1 = models.CharField(max_length=50, default="N/A")
    responsable_intervention2 = models.CharField(max_length=50, default="N/A")
    responsable_intervention3 = models.CharField(max_length=50, default="N/A")
    
    nombre_intervenant = models.IntegerField(default=0)
    
    # B-7 AUTRES INSTRUCTIONS ET MESURE PREVENTIVE
    autre_instruction = models.CharField(max_length=200, default="N/A")
    
    numero_urgence = models.CharField(max_length=50, default="N/A")
    
    # B-8 VALIDATION AVANT LES TRAVAUX
    # REPRESENTANT DES INTERVENANT
    nom_representant_intervenant1 = models.CharField(max_length=50, default="N/A")
    nom_representant_intervenant2 = models.CharField(max_length=50, default="N/A")
    
    # RESPONSABLE DU SITE D'INTERVENTION
    nom_site_intervention = models.CharField(max_length=50, default="N/A")
    date_site_intervention = models.DateField(default=date.today)
    visa_site_intervention = models.CharField(max_length=20, default="N/A")
    
    # B-9 VALIDATION APRES LES TRAVAUX
    travail_temine = models.BooleanField(default=False)
    site_laisse_normale = models.BooleanField(default=False)
    
    travail_non_termine = models.BooleanField(default=False)
    site_laisse_propre = models.BooleanField(default=False)
    
    # RESPONSABLE DU SITE D'INTERVENTION
    nom_site_intervention_fin = models.CharField(max_length=50, default="N/A")
    date_heure_site_intervention = models.DateTimeField(default=datetime.now)
    
    # REPRESENTANT DES INTERVENANTS 
    nom_representant_intervenant_fin = models.CharField(max_length=50, default="N/A")
    date_representant_intervenant_fin = models.DateTimeField(default=datetime.now)
    
    
    def __str__(self):
        return str(self.user_profile)
    
    class Meta:
        verbose_name = "Checklist Station"
        verbose_name_plural = "Checklist Station"
    
class nature_risque(models.Model):
    emission_gaz = models.BooleanField(default=False)
    incendie = models.BooleanField(default=False)
    explosion = models.BooleanField(default=False)
    projection_etincelle = models.BooleanField(default=False)
    intoxication = models.BooleanField(default=False)
    asphyxie = models.BooleanField(default=False)
    brulure = models.BooleanField(default=False)
    blessure = models.BooleanField(default=False)
    autre_lesion = models.BooleanField(default=False)
    chute_plain_pied = models.BooleanField(default=False)
    chute_objet = models.BooleanField(default=False)
    chute_hauteur = models.BooleanField(default=False)
    incident_reseau = models.BooleanField(default=False)
    epandage = models.BooleanField(default=False)
    eboulement = models.BooleanField(default=False)
    electrocution = models.BooleanField(default=False)
    incident_cable = models.BooleanField(default=False)
    accident_circulation = models.BooleanField(default=False)
    autre_lesion = models.CharField(max_length=200)

    


class checklist_permis_feu_prest(models.Model):
    user_profile_feu = models.CharField(max_length=200,default="N/A")
    
    date_entete     = models.DateField(auto_now_add=True)
    registre_entete = models.IntegerField()
    
    site            = models.CharField(max_length=200)
    client          = models.CharField(max_length=200)
    localite        = models.CharField(max_length=200)
    entreprise_intervenante = models.CharField(max_length=200)
    
    # Descriptif du travail
    descriptif_travail = models.CharField(max_length=200)
    
    date_debut          = models.DateField(auto_now_add=True)
    heure_debut         = models.TimeField(auto_now_add=True)
    heure_fin           = models.TimeField(auto_now_add=True)
    date_fin            = models.DateField(auto_now_add=True)
    
    # Risque particulier 
    proximite_zone_ATEX = models.BooleanField(default=False)
    autre_risque        = models.CharField(max_length=50)
    # Nom des intervenants autorisés
    intervenant1 = models.CharField(max_length=50)
    intervenant2 = models.CharField(max_length=50)
    intervenant3 = models.CharField(max_length=50)
    intervenant4 = models.CharField(max_length=50)
    
    # Type de travaux par points chauds
    soudage     = models.BooleanField(default=False)
    tronconnage = models.BooleanField(default=False)
    decoupage   = models.BooleanField(default=False)
    meulage     = models.BooleanField(default=False)
    autre_type_travaux = models.CharField(max_length=50)
    # Materiels utilises
    poste_souder    = models.BooleanField(default=False)
    chalumeau       = models.BooleanField(default=False)
    meuleuse        = models.BooleanField(default=False)
    tronconneuse    = models.BooleanField(default=False)
    autre_materiel_utilise = models.CharField(max_length=50)
    # Document associés
    plan_prevention = models.BooleanField(default=False)
    ASET            = models.BooleanField(default=False)
    permis_entree_espace_confine = models.BooleanField(default=False)
    autre_document  = models.CharField(max_length=50)
        
    evacuation_substance = models.CharField(max_length=10, default='N/A')
    balisage_perimetre = models.CharField(max_length=10, default='N/A')
    protection_element = models.CharField(max_length=10, default='N/A')
    consignation_equipement = models.CharField(max_length=10, default='N/A')
    vidange = models.CharField(max_length=10, default='N/A')
    degazage = models.CharField(max_length=10, default='N/A')
    isolation_tuyauterie = models.CharField(max_length=10, default='N/A')
    demontage_tuyauterie = models.CharField(max_length=10, default='N/A')
    
    
    # MOYENS DE PREVENTION
    ecran = models.CharField(max_length=10, default='N/A')
    bache = models.CharField(max_length=10, default='N/A')
    extincteur = models.CharField(max_length=10, default='N/A')
    sable = models.CharField(max_length=10, default='N/A')
    
    # VENTILATION FORCEE
    ventilation = models.CharField(max_length=10, default='N/A')
    
    #TEST ATMOSPHERIQUE
    test_atmospherique = models.CharField(max_length=10, default='N/A')
    
    teneur_oxygene = models.CharField(max_length=10, default='N/A')
    teneur_LIE = models.CharField(max_length=10, default='N/A')
    
    # Surveillance de sécurité pendant les travaux 
    nom_surveillance_pendant = models.CharField(max_length=100, default="N/A")
    
    # Surveillance de sécurité après les travaux
    heure_debut_surveillance = models.TimeField(blank=True , null=True)
    heure_fin_surveillance = models.TimeField(blank=True , null=True)
    nom_surveillance_apres = models.CharField(max_length=100, default="N/A")
    
    # ALERT EN CAS D'INCENDIE OU D'ACCIDENT
    alerte = models.CharField(max_length=200, default="N/A")
    
    # NUMERO D'URGENCE 
    numero_pompier = models.CharField(max_length=50, default="N/A")
    numero_site = models.CharField(max_length=50, default="N/A")
    numero_jovena = models.CharField(max_length=50, default="N/A")
    numero_ambulance = models.CharField(max_length=50, default="N/A")
    
    # PERSONNES OU SERVICES CONCERNES
    nom_responsable_travaux = models.CharField(max_length=50, default="N/A")
    qualite_responsable_travaux = models.CharField(max_length=50, default="N/A")
    visa_responsable_travaux = models.CharField(max_length=50, default="N/A")
    
    nom_responsable_HSE = models.CharField(max_length=50, default="N/A")
    qualite_responsable_HSE = models.CharField(max_length=50, default="N/A")
    visa_responsable_HSE = models.CharField(max_length=50, default="N/A")
    
    nom_responsable_site = models.CharField(max_length=50, default="N/A")
    qualite_responsable_site = models.CharField(max_length=50, default="N/A")
    visa_responsable_site = models.CharField(max_length=50, default="N/A")
    
    nom_responsable_autre = models.CharField(max_length=50, default="N/A")
    qualite_responsable_autre = models.CharField(max_length=50, default="N/A")
    visa_responsable_autre = models.CharField(max_length=50, default="N/A")
    
    CHOICES_VALIDATION = (
    ('en_attente', 'En attente de réponse'),
    ('confirme', 'Confirmé'),
    ('refuse', 'Refusé'),
)
    
    validation = models.CharField(
        max_length=15,
        choices=CHOICES_VALIDATION,
        default='en_attente',  # Par défaut, en attente de réponse
    )
    
    permis_feu_delivre = models.DateField(default=date.today)
    
    def __str__(self):
        return self.user_profile_feu
    
    class Meta:
        verbose_name = "Permis Feu"
        verbose_name_plural = "Permis Feu"
    
class checklist_excavation(models.Model):
    user_profile_excavation=models.CharField(max_length=200 , default="N/A")
    
    # ENTETE
    date_entete = models.DateField(auto_now_add=True)
    Registre_entete = models.IntegerField()
    
    # HEADER
    site = models.CharField(max_length=50)
    localite = models.CharField(max_length=100)
    client = models.CharField(max_length=50)
    entreprise_intervenante = models.CharField(max_length=100)
    
    # Descriptif du travail
    descriptif = models.CharField(max_length=500, default='N/A')
    profondeur_excavation = models.CharField(max_length=50)
    zone = models.CharField(max_length=50)
    
    type_excavation = models.CharField(max_length=10, default='N/A')
    dessin1 = models.CharField(max_length=50, default='N/A')
    dessin2 = models.CharField(max_length=50, default='N/A')
    dessin3 = models.CharField(max_length=50, default='N/A')
    dessin4 = models.CharField(max_length=50, default='N/A')
    
    # Obstruction Souterraines
    eau_incendie = models.BooleanField(default=False)
    eau_pluviale = models.BooleanField(default=False)
    eau_riviere = models.BooleanField(default=False)
    effluent = models.BooleanField(default=False)
    eau_domestique = models.BooleanField(default=False)
    sanitaire = models.BooleanField(default=False)
    
    cable_communication = models.BooleanField(default=False)
    mise_terre = models.BooleanField(default=False)
    structure_adjacente = models.BooleanField(default=False)
    cable_cathodique = models.BooleanField(default=False)
    ligne_gaz = models.BooleanField(default=False)
    atre_obstruction = models.BooleanField(default=False)
    
    electrique_11kv = models.BooleanField(default=False)
    electrique_6kv = models.BooleanField(default=False)
    electrique_690v = models.BooleanField(default=False)
    electrique_690i = models.BooleanField(default=False)
    
    commentaire_obstruction1 = models.CharField(max_length=50, default='N/A')
    commentaire_obstruction2 = models.CharField(max_length=50, default='N/A')
    commentaire_obstruction3 = models.CharField(max_length=50, default='N/A')
    commentaire_obstruction4 = models.CharField(max_length=50, default='N/A')
    commentaire_obstruction5 = models.CharField(max_length=50, default='N/A')
    commentaire_obstruction6 = models.CharField(max_length=50, default='N/A')
    
    # Consideration Specifiques
    pente = models.BooleanField(default=False)
    banc = models.BooleanField(default=False)
    etayage = models.BooleanField(default=False)
    pretection_nuit = models.BooleanField(default=False)
    pretection_ouverture = models.BooleanField(default=False)
    permis_espace = models.BooleanField(default=False)
    pompage_eau = models.BooleanField(default=False)
    fermeture_route = models.BooleanField(default=False)
    
    mesure_securite_additionnel = models.CharField(max_length=100, default='N/A')
    commentaire1 = models.CharField(max_length=50, default='N/A')
    commentaire2 = models.CharField(max_length=50, default='N/A')
    commentaire3 = models.CharField(max_length=50, default='N/A')
    commentaire4 = models.CharField(max_length=50, default='N/A')
    
    # DETECTION DES STRUCTURES ET SERVICES NON-APPARENTS
    effectuee = models.BooleanField(default=False)
    effectuer_nom = models.CharField(max_length=200, default="N/A")
    effectuer_date = models.DateField(default=date.today)
    # effectuer_signature = models.CharField(max_length=200, default="N/A")
    
    representant_contracant = models.BooleanField(default=False)
    representant_contracant_nom = models.CharField(max_length=200, default="N/A")
    representant_contracant_date = models.DateField(default=date.today)
    # representant_contracant_signature = models.CharField(max_length=200, default="N/A")
    
    # APPROBATION 
    superviseur_nom = models.CharField(max_length=200, default="N/A")
    superviseur_date = models.DateField(default=date.today)
    
    representant_proprietaire_nom = models.CharField(max_length=200, default="N/A")
    representant_proprietaire_date = models.DateField(default=date.today)
    # representant_proprietaire_signature = models.CharField(max_length=200, default="N/A")
    
    # ACCORD
    superviseur_excavation_nom = models.CharField(max_length=200, default="N/A")
    superviseur_excavation_date = models.DateField(default=date.today)
    # superviseur_signature = models.CharField(max_length=200, default="N/A")
    
    # ACHIEVEMENT DE L'EXCAVATION
    date_achevement_excavation = models.DateField(default=date.today)
    # signature_achevement = models.CharField(max_length=200, default="N/A")
    
    CHOICES_VALIDATION = (
    ('en_attente', 'En attente de réponse'),
    ('confirme', 'Confirmé'),
    ('refuse', 'Refusé'),
)
    
    validation = models.CharField(
        max_length=15,
        choices=CHOICES_VALIDATION,
        default='en_attente',  # Par défaut, en attente de réponse
    )
    
    # FIN
    permis_excavation_delivre = models.DateField(default=date.today)
      
    def __str__(self):
        return self.user_profile_excavation
    
    class Meta:
        verbose_name = "Permis Excavation"
        verbose_name_plural = "Permis Excavation"
    

class checklist_espace_confinez(models.Model):
    user_profile_confine=models.CharField(max_length=200, default="N/A")
    
    # ENTETE
    date_entete = models.DateField(default=date.today)
    registre_entete = models.IntegerField()
    
    # DESCRIPTION DU TRAVAIL
    site = models.CharField(max_length=200, default="N/A")
    equipement = models.CharField(max_length=50, default="N/A")
    entreprise_intervenante = models.CharField(max_length=50, default="N/A")
    
    date_debut = models.DateField(default=date.today)
    heure_debut = models.TimeField(blank=True , null=True)
    heure_fin = models.TimeField(blank=True , null=True)
    date_fin = models.DateField(default=date.today)
    
    descriptif_travail = models.CharField(("Descriptif du travail"), max_length=50, default="N/A")    
    
    # 2. PREPARATION DE L'INTERVENTION
    consignation_electique = models.BooleanField(default=False)
    consignation_fluidique = models.BooleanField(default=False)
    consignation_mecanique = models.BooleanField(default=False)
    ventilation = models.BooleanField(default=False)
    ventilation_forcee = models.BooleanField(default=False)
    plan_urgence = models.BooleanField(default=False)
    ASET = models.BooleanField(default=False)
    autre_intervention = models.CharField(max_length=200, default="N/A")
    
    # 3. EQUIPEMENT DE SECURITE 
    detecteur_gaz = models.BooleanField(default=False)
    type_detecteur_gaz = models.CharField(max_length=50, default="N/A")
    
    appareil_respiratoire_autonome = models.BooleanField(default=False)
    type_appareil_respiratoire_autonome = models.CharField(max_length=50, default="N/A")
    
    appareil_respiratoire_isolant = models.BooleanField(default=False)
    type_appareil_respiratoire_isolant = models.CharField(max_length=50, default="N/A")
    
    masque = models.BooleanField(default=False)
    type_masque = models.CharField(max_length=50, default="N/A")
    
    harnais = models.BooleanField(default=False)
    type_harnais = models.CharField(max_length=50, default="N/A")
    
    treuil = models.BooleanField(default=False)
    type_treuil = models.CharField(max_length=50, default="N/A")
    
    corde_assurance = models.BooleanField(default=False)
    type_corde_assurance = models.CharField(max_length=50, default="N/A")
    
    panneaux = models.BooleanField(default=False)
    type_panneaux = models.CharField(max_length=50, default="N/A")
    
    balisage = models.BooleanField(default=False)
    type_balisage = models.CharField(max_length=50, default="N/A")
    
    moyen_intervenant = models.CharField(max_length=200, default="N/A")
    
    # 4. QUALITE DE L'AIR
    # O2
    o2_applicable = models.BooleanField(default=False)
    o2_date = models.DateField(default=date.today)
    o2_heure1 = models.TimeField(blank=True , null=True)
    o2_PPM1 = models.CharField(max_length=10, default="N/A")
    o2_heure2 = models.TimeField(blank=True , null=True)
    o2_PPM2 = models.CharField(max_length=10, default="N/A")
    o2_heure3 = models.TimeField(blank=True , null=True)
    o2_PPM3 = models.CharField(max_length=10, default="N/A")
    
    # %LIE
    LIE_applicable = models.BooleanField(default=False)
    LIE_date = models.DateField(default=date.today)
    LIE_heure1 = models.TimeField(blank=True , null=True)
    LIE_PPM1 = models.CharField(max_length=10, default="N/A")
    LIE_heure2 = models.TimeField(blank=True , null=True)
    LIE_PPM2 = models.CharField(max_length=10, default="N/A")
    LIE_heure3 = models.TimeField(blank=True , null=True)
    LIE_PPM3 = models.CharField(max_length=10, default="N/A")
    
    # Co
    Co_applicable = models.BooleanField(default=False)
    Co_date = models.DateField(default=date.today)
    Co_heure1 = models.TimeField(blank=True , null=True)
    Co_PPM1 = models.CharField(max_length=10, default="N/A")
    Co_heure2 = models.TimeField(blank=True , null=True)
    Co_PPM2 = models.CharField(max_length=10, default="N/A")
    Co_heure3 = models.TimeField(blank=True , null=True)
    Co_PPM3 = models.CharField(max_length=10, default="N/A")
    
    # SO2
    SO_applicable = models.BooleanField(default=False)
    SO_date = models.DateField(default=date.today)
    SO_heure1 = models.TimeField(blank=True , null=True)
    SO_PPM1 = models.CharField(max_length=10, default="N/A")
    SO_heure2 = models.TimeField(blank=True , null=True)
    SO_PPM2 = models.CharField(max_length=10, default="N/A")
    SO_heure3 = models.TimeField(blank=True , null=True)
    SO_PPM3 = models.CharField(max_length=10, default="N/A")
    
    # H2S
    H2S_applicable = models.BooleanField(default=False)
    H2S_date = models.DateField(default=date.today)
    H2S_heure1 = models.TimeField(blank=True , null=True)
    H2S_PPM1 = models.CharField(max_length=10, default="N/A")
    H2S_heure2 = models.TimeField(blank=True , null=True)
    H2S_PPM2 = models.CharField(max_length=10, default="N/A")
    H2S_heure3 = models.TimeField(blank=True , null=True)
    H2S_PPM3 = models.CharField(max_length=10, default="N/A")
    
    # NH3
    NH3_applicable = models.BooleanField(default=False)
    NH3_date = models.DateField(default=date.today)
    NH3_heure1 = models.TimeField(blank=True , null=True)
    NH3_PPM1 = models.CharField(max_length=10, default="N/A")
    NH3_heure2 = models.TimeField(blank=True , null=True)
    NH3_PPM2 = models.CharField(max_length=10, default="N/A")
    NH3_heure3 = models.TimeField(blank=True , null=True)
    NH3_PPM3 = models.CharField(max_length=10, default="N/A")
    
    nom_testeur = models.CharField(("Nom du testeur de Gaz"), max_length=50, default="N/A")
    # signature_testeur = models.CharField(max_length=500, default="N/A") 
     
    # 4. AUTORISATION (Responsable Jovena)
    nom_reponsable_jovena = models.CharField(max_length=100, default="N/A")
    date_heure1 = models.DateTimeField(default=datetime.now)
    
    # 5. SURVEILLANT DE L'ESPACE CONFINE
    nom_surveillant = models.CharField(("Nom du surveillant"), max_length=50, default="N/A")
    date_heure2 = models.DateTimeField(default=datetime.now)
    
    # 6. CLOTURE DU PERMIS (Responsable habilité de l'entreprise intervaenante)
    nom_cloture = models.CharField(("Nom du responsable habilité"), max_length=50, default="N/A")
    date_heure3 = models.DateTimeField(default=datetime.now)
    
    # ALERTE EN CAS D'INCIDENT
    alerte = models.CharField(max_length=200, default="N/A")
    
    # NUMERO D'URGENCE
    pompier = models.CharField(max_length=50, default="N/A")
    ambulance = models.CharField(max_length=50, default="N/A")
    responsable_site = models.CharField(max_length=50, default="N/A")
    responsable_jovena = models.CharField(max_length=50, default="N/A")
    
    CHOICES_VALIDATION = (
    ('en_attente', 'En attente de réponse'),
    ('confirme', 'Confirmé'),
    ('refuse', 'Refusé'),
)
    
    validation = models.CharField(
        max_length=15,
        choices=CHOICES_VALIDATION,
        default='en_attente',  # Par défaut, en attente de réponse
    )
    
    # FIN
    permi_delivre = models.DateField(default=date.today)
           
    
    def __str__(self):
        return self.user_profile_confine
    
    class Meta:
        verbose_name = "Espace Confiner"
        verbose_name_plural = "Espace Confiner"

