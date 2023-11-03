from ast import Break

from django.contrib import admin

from django.http            import HttpResponse
from django.http.request    import HttpRequest
from django.http.response   import HttpResponse

from django.contrib.admin import AdminSite

from django.db.models   import QuerySet
from app.models         import UserProfile
from    .models         import *

from django.contrib.auth.models import User
from django.contrib.auth.admin  import UserAdmin as AuthUserAdmin

from reportlab.pdfgen           import canvas
from reportlab.platypus         import Table, TableStyle ,SimpleDocTemplate, Image
from reportlab.lib              import colors
from reportlab.lib.pagesizes    import letter
from reportlab.platypus         import Paragraph
from reportlab.lib.styles       import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.pagesizes    import A3

from django.utils import timezone


# Register your models here.
class UserProfileInline(admin.StackedInline):
    model = UserProfile
    can_delete = False
    
    
class AccountsUserAdmin(AuthUserAdmin):
    def add_view(self, *args, **kwargs): 
       self.inlines = []
       return super(AccountsUserAdmin , self).add_view(*args, **kwargs)
    
    def change_view(self, *args, **kwargs):
        self.inlines = [UserProfileInline]
        return super(AccountsUserAdmin , self).change_view(*args, **kwargs)
   
  
image_path = 'static/images/jovena.jpg'   
logo = Image(image_path, width=150, height=43)


   
   
'''
PDF CHECKLIST STATION SERVICE
'''   
   
class ChecklistStatAdmin(admin.ModelAdmin):
    actions = ['generate_pdf']

    def generate_pdf(self, request, queryset):
        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="formulaire.pdf"'

        # Créez un objet SimpleDocTemplate pour le PDF
        doc = SimpleDocTemplate(response, pagesize=A3)
        
        style_bold = ParagraphStyle(name='BoldStyle', parent=getSampleStyleSheet()['Normal'])
        style_bold.fontName = 'Helvetica-Bold'
        
        style_head = ParagraphStyle(name='BoldStyle', parent=getSampleStyleSheet()['Normal'])
        style_head.fontName = 'Helvetica-Bold'

        # Créez une liste pour stocker les données du tableau
        table_data1 = []
        table_data2 = []
        table_data3 = []
        table_data4 = []
        table_data5 = []
        table_data6 = []
        table_data7 = []
        table_data8 = []
        table_data9 = []
        
        diag = []
        prev = []
        st_B1 = []
        st_B2 = []
        local = []
        
        table_data01 = []
        table_data22 = []
        table_data10 = []
        table_data11 = []
        table_data12 = []
        table_data13 = []
        table_data14 = []
        table_data31 = []
        table_data81 = []
        table_data82 = []
        table_data83 = []
        table_data84 = []
        
        table_vide = []

        for obj in queryset:
            # Ajoutez les données de chaque objet sous forme de liste
            
            row = [f'']
            table_vide.append(row)
            
            row = [logo, f'ITM / FORMADIAPPJ / V2.00', f'Date: ..... ']
            table_data01.append(row)
            
            row = ['', f'FORMULAIRE DE DIAGNOSTIC ET DE PLAN DE PREVENTION JOURNALIER', f'Registre: ......']
            table_data01.append(row)
            
            row = [Paragraph('A- DIAGNOSTIC', style_bold)]
            diag.append(row)
            
            
            row = [f"N réclamation: {obj. num_reclamation  }", f"Date et heure du diagnostic: {obj.date_diagnostic}"]
            table_data1.append(row)

            row = [f"panne annoncée: {obj.panne_annoncee}", f"Interlocuteur: {obj.interlocuteur}"]
            table_data1.append(row)

            row =[f"site:{obj.site}                         " f"                                                             Client:{obj.client}",f"Fonction:{obj.fonction}"]
            table_data1.append(row)
            
            # row = [f" Localité: {obj.localite} \n Entreprise intervenante: {obj.entreprise_intervenante} \n Catégorie de réclamation: {obj.categorie_reclamation} \n Date de réclamation: {obj.date_reclamation} \n Echéance: {obj.echeance} " ,
            #        f"Panne réelle:{obj.panne_reel} \n \n \n \n  "]
            # table_data1.append(row)
            
            row = [f"Localité:   {obj.localite}", Paragraph("Panne réelle:", style_bold), f"Responsable maintenance",]
            local.append(row)
            
            row = [f"Entreprise intervenante:   {obj.entreprise_intervenante}", f'{obj.panne_reel}', f'']
            local.append(row)
            
            row = [f"Catégorie de réclamation:   {obj.categorie_reclamation}", f'', f'']
            local.append(row)
            
            row = [f"Date de réclamation:   {obj.date_reclamation  }", f'', f'']
            local.append(row)
            
            row = [f"Echeance:   {obj.echeance}", f'', f'']
            local.append(row)
            
            row=[Paragraph("B-PLAN DE PREVENTION HSE", style_bold)]
            prev.append(row)
            
            row = [Paragraph("B-1 RISQUE D'INTERFERENCE AVEC L'INTERVENTION", style_bold)]
            st_B1.append(row)
            
            row = [f"   Livraison de carburant (dépotage) prévue le:        {obj.livraison_carburant.strftime('%d/%m/%Y' '      à     %H:%M')} \n"
                   f"   Présence dans la zone de travail de:        {obj.presence_zone} \n"
                    f"   Autres travaux prévus ce jour:         {obj.autre_travaux}"]
            table_data2.append(row)
            
            row = [Paragraph("B-2 MESURES DE SECURITE  OBLIGATOIRES ", style_bold)]
            st_B2.append(row)
            
            row = [f" {'[x]' if obj.permis_specifique else '[  ]'} Permis spécifiques pour les travaux à chaud et entrée en espace confiné \n {'[x]' if obj.information_personnel else '[  ]'} Information du personnel et visiteurs présents sur le lieu d'intervention \n {'[x]' if obj.port_EPI else '[  ]'} Port EPI de base (casque, lunettes, chaussures de sécurité, habits à bande refléchissante)" ,
                   f" {'[x]' if obj.balisage_perimetre else '[  ]'} Balisage du périmètre de sécurité du lieu d'intervention\n {'[x]' if obj.extincteur_adapte else '[  ]'} Extincteurs adaptés \n {'[x]' if obj.interdiction_de_fumer else '[  ]'} Interdiction de fumer et de télephoner dans les zones à risque"]
            table_data22.append(row)
            
            row = [Paragraph("B-3 NATURE DU TRAVAIL", style_bold) , Paragraph("B-4 NATURE DES RISQUES", style_bold) , Paragraph("B-5 MESURES PREVENTIVES", style_bold)]
            table_data31.append(row)
            
            row = [f" {'[x]' if obj.travail_chaud else '[  ]'}   Travail à chaud \n { '[x]'if obj.percage_moulage_decoupage else '[  ]'}   Perçage, moulage, découpage \n { '[x]' if obj.chauffage_soudage else '[  ]'}   Chauffage, soudage \n {'[x]' if obj.grenaillage_sablage else '[  ]'}   Grenaillage, sablage  \n {'[x]' if obj.utilisation_equipement else '[  ]'}   Utilisation d' équipement électroportatif \n {'[x]' if obj.vidange_degazage else '[  ]'}   Vidange/ dégazage/ nettoyage \n { '[x]' if obj.travaux_demolition else '[  ]'}   Travaux de démolition \n {'[x]' if obj.travail_espace else '[  ]'}   Travail en espace confiné \n {'[x]' if obj.deplacement_site else '[  ]'}   Déplacement sur site \n { '[x]' if obj.manutention_levage else '[  ]'}   Manutention/levage \n { '[x]' if obj.travail_hauteur else '[  ]'}   Travail en hauteur > 1,80m \n { '[x]' if obj.travail_tuyauterie else '[  ]'}   Travail sur tuyauterie/ appareil de distribution \n {'[x]' if obj.fouille_mannuelle else '[  ]'}   Fouille manuelle \n { '[x]' if obj.travaux_excavation else '[  ]'}   Travaux d'excavation \n { '[x]' if obj.travail_equipement else '[  ]'}   Travail sur équipement électrique \n { '[x]' if obj.travail_engin else '[  ]'}   Travail avec engin de chantier \n {'[x]' if obj.operation_piste else '[  ]'}   Opérations sur piste \n {'[x]' if obj.travaux_bruyant else '[  ]'}   Travaux bruyants \n \n Autres (à préciser): \n {obj.autre_nature}",
                   f" {'[x]' if obj.emission_gaz else '[  ]'}   Emission de gaz toxiques \n {'[x]' if obj.incendie else '[  ]'}   Incendie \n {'[x]' if obj.explosion else '[  ]'}   Explosion \n {'[x]' if obj.projection_etincelle else '[  ]'}   Projection d'étincelles/particules \n {'[x]' if obj.intoxication else '[  ]'}   Intoxication \n {'[x]' if obj.asphyxie else '[  ]'}   Asphyxie \n {'[x]' if obj.brulure else '[  ]'}   Brulures \n {'[x]' if obj.blessure else '[  ]'}   Blessures \n {'[x]' if obj.autre_lesion else '[  ]'}   Autres lésions \n {'[x]' if obj.chute_plain_pied else '[  ]'}   Chute de plain-pied \n {'[x]' if obj.chute_objet else '[  ]'}   Chute d'objet \n {'[x]' if obj.chute_hauteur else '[  ]'}   Chute de hauteur \n {'[x]' if obj.incident_reseau else '[  ]'}   Incidents réseau enterré \n {'[x]' if obj.epandage else '[  ]'}   Epandage \n {'[x]' if obj.eboulement else '[  ]'}   Eboulement/ensevelissement \n {'[x]' if obj.electrocution else '[  ]'}   Electrocution/Electricistion \n {'[x]' if obj.incident_cable else '[  ]'}   Incidents cable aériens \n {'[x]' if obj.accident_circulation else '[  ]'}   Accident lié à la circulation \n \n Autres Lésions \n {obj.autre_lesion}",
                   f"   A la charge de la station-service     -    {obj.charge_station_service} \n   Arret de la distribution     -    { obj.arret_distribution_total }\n {'[x]' if obj.fermeture_station else '[  ]'}   Fermeture de la station \n {'[x]' if obj.arret_activite else '[  ]'}   Arret d'une activité (précisez) \n \n A la charge de la/les entreprise(s) extérieur(s) \n {'[x]' if obj.test_gaz else '[  ]'}   Test de gaz \n {'[x]' if obj.arret_travaux_depotage else '[  ]'}   Arret des travaux pendant le dépotage \n {'[x]' if obj.arret_autre_travaux else '[  ]'}   Arret des autres travaux prévus \n {'[x]' if obj.extincteur_adapte2 else '[  ]'}   Extincteurs adaptés \n {'[x]' if obj.mise_terre else '[  ]'}   Mise à la terre correcte des équipements \n {'[x]' if obj.appareil_respiratoire else '[  ]'}   Appareil respiratoire, ventilateur \n {'[x]' if obj.outillage else '[  ]'}   Outillage/Eclairage/Ventilateur \n {'[x]' if obj.port_EPI_2 else '[  ]'}   Port EPI spécifiques (précisez) \n {'[x]' if obj.harnai else '[  ]'}   Harnais et dispositif anti-chute \n {'[x]' if obj.echaffaudage else '[  ]'}   Echaffaudage approprié \n {'[x]' if obj.renseignement_reseaux_enterre else '[  ]'}   Renseignements sur réseaux enterrés \n {'[x]' if obj.consignation_equipement else '[  ]'}   Consignation équipement ou système \n {'[x]' if obj.consignation_electrique else '[  ]'}   Consignation électrique \n {'[x]' if obj.renseignement_reseau_aerien else '[  ]'}   Renseignements sur réseau aérien \n {'[x]' if obj.aide_circulation else '[  ]'}   Aide à la circulation "]
            table_data3.append(row)
            # Ajoutez d'autres champs de votre modèle ici
            
            row = [Paragraph("B-6 VISAS (Partie à remplir conjoitement pa un responsable du site et par l'entreprise intervenante avant le début des travaux)", style_bold)]
            table_data4.append(row)
            
            row = [Paragraph('Entreprise utilisatrice (station, client conso ou autre)', style_bold), Paragraph('Entreprise(s) extérieure(s) intervenante(s) (y compris les sous-traitants)', style_bold)]
            table_data5.append(row)
            
            row = [f"Cachet commercial de l'entreprise utilisatrice", f"Responsable de l'intervention", f"Nb d'intervenants: {obj.nombre_intervenant}", f"Chef d'atelier"]
            table_data6.append(row)       
            
            row = [f' \n \n ',
                   f' 1: {obj.responsable_intervention1} \n 2: {obj.responsable_intervention2} \n 3: {obj.responsable_intervention3}', 
                   f' \n \n ']  
            table_data7.append(row)   
            
            row = [Paragraph('B-7 AUTRES INSTRUCTIONS ET MESURES PREVENTIVES AUX INTERVENANTS', style_bold)]
            table_data81.append(row)
            
            row = [f' {obj.autre_instruction} \n \n']
            table_data82.append(row)
            
            row = [f"Numéro d'urgence: {obj.numero_urgence}"]
            table_data83.append(row)
            
            row = [Paragraph("B-8 VALIDATION AVANT LES TRAVAUX", style_bold)]
            table_data84.append(row)
            
            row = [f'REPRESENTANT DES INTERVENANTS', f"RESPONSABLE DI SITE D'INTERVENTION"]
            table_data9.append(row)
            
            row = [f' 1. Nom: {obj.nom_representant_intervenant1} \n 2. Nom: {obj.nom_representant_intervenant2}', f' Nom: {obj.nom_site_intervention} ' f'                          Signature: ......\n Date: {obj.date_site_intervention} ' f'                            Visa: {obj.visa_site_intervention}' ]
            table_data10.append(row)
            
            row = [Paragraph('B-9 VALIDATION APRES LES TRAVAUX', style_bold)]
            table_data11.append(row)
            
            # row = [f'Le travail est terminé {obj.travail_temine} \n La site est rendu exploitation normale {obj.site_laisse_normale}',
            #        f"Le travail n'est pas terminé  {obj.travail_non_termine} \n Le site a été laissé propre et en sécurité {obj.site_laisse_propre} "]
            # table_data12.append(row)
            
            row = [' Le travail est terminé \n La site est rendu exploitation normale', 
                   f" {'[x]' if obj.travail_temine else '[  ]'} \n {'[x]' if obj.site_laisse_normale else '[  ]'}",
                   " Le travail n'est pas terminé \n Le site a été laissé propre et en sécurité",
                   f" {'[x]' if obj.travail_non_termine else '[  ]'} \n {'[x]' if obj.site_laisse_propre else '[  ]'}"]
            table_data12.append(row)
            
            row = [f"RESPONSABLE DU SITE D'INTERVENTION", f"REPRESENTANT DES INTERVENANTS"]
            table_data13.append(row)
            
            row = [f"Nom: {obj.nom_site_intervention_fin}" f"                             Signature: .......... \n Date et heure: {obj.date_heure_site_intervention.strftime('%d/%m/%Y' '      à     %H:%M')}",
                   f"Nom: {obj.nom_representant_intervenant_fin}" f"                             Signature: .......... \n Date {obj.date_representant_intervenant_fin.strftime('%d/%m%Y' '        à        %H:%M')} "]
            table_data14.append(row)

        # Créez le tableau avec les données
        table01 = Table(table_data01, colWidths=[174, 450, 174])        
        
        diagno = Table(diag, colWidths=[798])
        prevention = Table(prev, colWidths=[798])
        B1 = Table(st_B1, colWidths=[798])
        B2 = Table(st_B2, colWidths=[798])
        localite = Table(local, colWidths=[399, 210, 189])
        
        table1 = Table(table_data1, colWidths=[399, 399])
        table2 = Table(table_data2, colWidths=[798])
        table3 = Table(table_data3, colWidths=[266 , 266 , 266])
        table4 = Table(table_data4, colWidths=[798])
        table5 = Table(table_data5, colWidths=[266, 532])
        table6 = Table(table_data6, colWidths=[266, 185, 173, 174])
        table7 = Table(table_data7, colWidths=[266, 358, 174])
        table9 = Table(table_data9, colWidths=[399, 399])
        
        table22 = Table(table_data22, colWidths=[450,348])
        table10 = Table(table_data10, colWidths=[399, 399])
        table11 = Table(table_data11, colWidths=[798])
        table12 = Table(table_data12, colWidths=[375, 24, 375, 24])
        table13 = Table(table_data13, colWidths=[399, 399])
        table14 = Table(table_data14, colWidths=[399, 399])
        table31 = Table(table_data31, colWidths=[266 , 266 , 266])
        table81 = Table(table_data81, colWidths=[798])
        table82 = Table(table_data82, colWidths=[798])
        table83 = Table(table_data83, colWidths=[798])
        table84 = Table(table_data84, colWidths=[798])
        
        
        
        vide = Table(table_vide, colWidths=[798])

        # Définissez le style du tableau, y compris les lignes
        style01 = TableStyle([
            # ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
            # ('ALIGN', (0, 0), (0, 0), 'CENTER'),
            ('ALIGN', (1,0), (1,0), 'CENTER'),
            ('ALIGN', (1,0), (1,1), 'CENTER'),
            ('BOTTOMPADDING', (0, 0), (-1, -1), 7),
            ('BOTTOMPADDING', (0, 0), (0, 0), -23),
            # ('FONTNAME', (0,0), (0,0), 'DarkGardenMK'),
            ('FONTNAME', (1,0), (1,0), 'Helvetica-Bold'),
            ('FONTNAME', (1,0), (1,1), 'Helvetica-Bold'),
            ('GRID', (1, 0), (-1, -1), 0.5, colors.black),
            ('BOX', (0,0), (-1,-1), 0.5, colors.black),
        ])
        
        style12 = TableStyle([
            ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
            ('BOTTOMPADDING', (0, 0), (-1, -1), 5),
            #('GRID', (0, 0), (-1, -1), 0.5, colors.black),
            ('BOX', (0,0), (1,0), 0.5, colors.black),
            ('BOX', (2,0), (3,0), 0.5, colors.black),
        ])
        
        styleLocal = TableStyle([
            ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
            ('BOTTOMPADDING', (0, 0), (-1, -1), 5),
            # ('GRID', (0, 0), (-1, -1), 0.5, colors.black),
            ('GRID', (0,0), (0,4), 0.5, colors.black),
            ('BOX', (1,0), (1,4), 0.5, colors.black),
            ('BOX', (2,0), (2,4), 0.5, colors.black),
            ('BOX', (2,0), (2,0), 0.5, colors.black),
            ('BACKGROUND', (2,0), (2,0), colors.lightgrey),
            ('FONTNAME', (2,0), (2,0), 'Courier-Bold'),
            ('ALIGN', (2, 0), (2, 0), 'CENTER'),
        ])
        
        style = TableStyle([
            ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
            ('BOTTOMPADDING', (0, 0), (-1, -1), 5),
            ('GRID', (0, 0), (-1, -1), 0.5, colors.black),
        ])
          
        styleYellow = TableStyle([
            ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
            ('BOTTOMPADDING', (0, 0), (-1, -1), 9),
            ('GRID', (0, 0), (-1, -1), 1, colors.black),
            ('BACKGROUND', (0,0), (-1,-1), colors.yellow),
        ])

        styleSilver = TableStyle([
            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
            ('BOTTOMPADDING', (0, 0), (-1, -1), 9),
            ('GRID', (0, 0), (-1, -1), 1, colors.black),
            ('BACKGROUND', (0,0), (-1,-1), colors.silver),
        ])
        
        styleRed = TableStyle([
            ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
            ('BOTTOMPADDING', (0, 0), (-1, -1), 5),
            ('GRID', (0, 0), (-1, -1), 1, colors.black),
            ('BACKGROUND', (0,0), (-1,-1), colors.red),
            ('FONTSIZE', (0,0),(0,0), 12),
        ])

        style22 = TableStyle([
            ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
            ('BOTTOMPADDING', (0, 0), (-1, -1), 5),
            ('BOX', (0,0), (-1,-1), 0.5, colors.black),
        ])
        
        style9 = TableStyle([
            ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
            ('BOTTOMPADDING', (0, 0), (-1, -1), 5),
            ('GRID', (0,0), (-1,-1), 0.5, colors.black),
            ('BACKGROUND', (0,0), (-1,-1), colors.lightgrey),
        ])

        style6 = TableStyle([
            ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
            ('BOTTOMPADDING', (0, 0), (-1, -1), 5),
            ('GRID', (0, 0), (-1, -1), 0.5, colors.black),
            ('BACKGROUND', (3,0), (3,0), colors.lightgrey),
            ('FONTNAME', (3,0), (3,0), 'Courier-Bold'),
            ('ALIGN', (3, 0), (3, 0), 'CENTER'),
        ])
            
        diagno.setStyle(styleYellow)
        prevention.setStyle(styleYellow)
        B1.setStyle(styleSilver)
        B2.setStyle(styleSilver)
        
        localite.setStyle(styleLocal)
        table1.setStyle(style)
        table2.setStyle(style)
        table3.setStyle(style)
        table4.setStyle(styleSilver)
        table5.setStyle(style)
        table6.setStyle(style6)
        table7.setStyle(style)
        table9.setStyle(style9)
        
        table31.setStyle(styleSilver)
        table01.setStyle(style01)
        table22.setStyle(style22)
        table10.setStyle(style)
        table11.setStyle(styleSilver)
        table12.setStyle(style12)
        table13.setStyle(style9)
        table14.setStyle(style)
        table81.setStyle(styleSilver)
        table82.setStyle(style)
        table83.setStyle(styleRed)
        table84.setStyle(styleSilver)
        
        
        vide.setStyle(style)

        # Construisez le PDF
        elements = [table01 ,vide, diagno ,table1, localite, prevention, B1, table2 , B2, table22 , table31, table3, table4, table5, table6, table7 ,table81, table82, table83 , table84, table9, table10 , table11, table12, table13, table14]
        doc.build(elements)

        return response

    generate_pdf.short_description = "Générer un PDF"
    




'''
PDF CHECKLIST PERMIS FEU
'''



class ChecklistPermisFeu(admin.ModelAdmin):
    actions = ['generate_pdf']
    
    def generate_pdf(self, request, queryset):
        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="formulaire.pdf"'

        # Créez un objet SimpleDocTemplate pour le PDF
        doc = SimpleDocTemplate(response, pagesize=A3)

        style_bold = ParagraphStyle(name='BoldStyle', parent=getSampleStyleSheet()['Normal'])
        style_bold.fontName = 'Helvetica-Bold'

        # Créez une liste pour stocker les données du tableau
        table_data0 = []
        table_data1 = []
        site = []
        table_data2 = []
        table_data3 = []
        table_data4 = []
        table_data5 = []
        table_data6 = []
        table_data7 = []
        table_data8 = []
        table_data9 = []
        table_data10 = []
        
        table_vide1 = []
        
        for obj in queryset:
            
            heure_debut_formatee = obj.heure_debut.strftime('%H:%M')
            heure_fin_formatee = obj.heure_fin.strftime('%H:%M')
            
            heure_debut_surveillance_formatee = obj.heure_debut_surveillance.strftime('%H:%M')
            heure_fin_surveillance_formatee = obj.heure_fin_surveillance.strftime('%H:%M')
                        
            # Ajoutez les données de chaque objet sous forme de liste
            
            # row = [Paragraph('1', style_bold), Paragraph('SGHSSES-TMP-JOV-903.1', style_bold), f'Date:{ obj.date_entete } ']
            # table_data1.append(row)
            
            # row = [f'2', Paragraph('PERMIS DE FEU', style_bold), f'Registre: { obj.registre_entete }']
            # table_data1.append(row)
            
            row = [logo, f'SGHSSES-TMP-JOV-903.1', f'Date:  { obj.date_entete } ']
            table_data1.append(row)
            
            row = ['', f'PERMIS DE FEU', f'Registre:  {obj.registre_entete}']
            table_data1.append(row)
            
            row = [f'Site: { obj.site }', f'Client: { obj.client }']
            site.append(row)
            row = [f'Localité: { obj.localite }', f'Entreprise intervenante: { obj.entreprise_intervenante }']
            site.append(row)
            
            row = [f'DESCRIPTION DU TRAVAIL: \n { obj.descriptif_travail } \n']
            table_data2.append(row)
            
            row = [f'Date de début: { obj.date_debut }', f'Heure de début: {heure_debut_formatee}' f'            Heure de fin: { heure_fin_formatee }', f'Date de fin: { obj.date_fin }']
            table_data3.append(row)
            
            row = [f'']
            table_vide1.append(row)
            
            row = [f'Risque particuliers', f'nom des intervenants autorisés']
            table_data4.append(row)
            
            row = [f' {"[x]" if obj.proximite_zone_ATEX else "[  ]" }   Proximité de zone ATEX \n \n         Autre(s) à préciser: \n         { obj.autre_risque } \n',
                   f' 1- { obj.intervenant1 } \n 2- { obj.intervenant2 } \n 3- { obj.intervenant3 } \n 4- { obj.intervenant4 } \n ']
            table_data4.append(row)
            
            row = [f'Type de travaux par points chauds', f'Matéels utilisés', f'Documents associés']
            table_data5.append(row)
            
            row = [f' {"[x]" if obj.soudage else "[  ]"} Soudage \n {"[x]" if obj.tronconnage else "[  ]" } Tronçonnage \n {"[x]" if obj.decoupage else "[  ]" } Découpage \n {"[x]" if obj.meulage else "[  ]"} Meulage \n\n Autre(s) à préciser \n {obj.autre_type_travaux}',
                   f' {"[x]" if obj.poste_souder else "[  ]" } Poste à souder \n {"[x]" if obj.chalumeau else "[  ]" } Chalumeau \n {"[x]" if obj.meuleuse  else "[  ]"} Meuleuse \n {"[x]" if obj.tronconneuse else "[  ]" } Tronçonneuse \n\n Autre(s) à préciser \n { obj.autre_materiel_utilise }',
                   f" {'[x]' if obj.plan_prevention else '[  ]'} Plan de prévention \n {'[x]' if obj.ASET else '[  ]'} ASET \n {'[x]' if obj.permis_entree_espace_confine else '[  ]'} Permis d'entrée en espace confiné \n\n Autre(s) à préciser \n { obj.autre_document }  \n "]
            table_data5.append(row)
            
            row = [f'MISE EN SECURITE', f'MOYENS DE PREVENTION']
            table_data6.append(row)
            
            row = [f'', f'Oui / Non / Fait', f'', f'Oui / Non / Fait']  
            table_data7.append(row)
            
            row = [f'Evacuation des substances combustibles', f'{obj.evacuation_substance}', f'Ecran, panneaux', f'{obj.ecran}']
            table_data7.append(row)
            
            row = [f'Balisage du périmètre de sécurité',f'{obj.balisage_perimetre}', f'Bâches ignifugées', f'{obj.bache}']
            table_data7.append(row)
            
            row = [f'Protection des éléments non déplaçables', f'{obj.protection_element}', f'Extincteurs adaptés ', f'{obj.extincteur}']
            table_data7.append(row)
            
            row = [f'Consignation équipement/électrique', f'{obj.consignation_equipement}', f'Sable', f'{obj.sable}']
            table_data7.append(row)
            
            row = [f'Vidange – nettoyage – dépoussiérage', f'{obj.vidange}', f'VENTILATION FORCEE', f'{obj.ventilation}']
            table_data7.append(row)
            
            row = [f'Dégazage (tuyauterie, cuve, citerne…)', f'{obj.degazage}', f'TEST ATMOSPHERIQUE', f'{obj.test_atmospherique}']
            table_data7.append(row)
            
            row = [f'Isolation des tuyauteries', f'{obj.isolation_tuyauterie}', f'Teneur en oxygène', f'{obj.teneur_oxygene}']
            table_data7.append(row)
            
            row = [f'Démontage de tuyauterie', f'{obj.demontage_tuyauterie}',  f'Teneur LIE', f'{obj.teneur_LIE}']
            table_data7.append(row)
            
            row = [f'Surveillance de sécurité pendant les travaux:', f'Surveillance de sécurité après les travaux']
            table_data8.append(row)
            
            row = [f" Nom et signature: \n {obj.nom_surveillance_pendant} \n \n \n  ",
                   f" A partir de {heure_debut_surveillance_formatee}   jusqu'à {heure_fin_surveillance_formatee}  \n \n Nom et Signature \n {obj.nom_surveillance_apres} \n"]
            table_data8.append(row)
            
            row = [f'ALERTE EN CAS D’INCENDIE OU D’ACCIDENT', f'NUMEROS D’URGENCE']
            table_data9.append(row)
            
            row = [f'\n \n', f' Pompier: {obj.numero_pompier}                                               Ambulance: {obj.numero_ambulance} \n Responsable du site: {obj.numero_site} \n Responsable Jovena: {obj.numero_jovena}']
            table_data9.append(row)
            
            row = [f'PERSONNES OU SERVICES CONCERNES', f'NOM', f'QUALITE', f'VISA']
            table_data10.append(row)
            
            row = [f'Responsable des travaux',f'{obj.nom_responsable_travaux}', f'{obj.qualite_responsable_travaux}', f'{obj.visa_responsable_travaux}']
            table_data10.append(row)
            
            row = [f'Responsable HSE ', f'{obj.nom_responsable_HSE}', f'{obj.qualite_responsable_HSE}', f'{obj.visa_responsable_HSE}']
            table_data10.append(row)
            
            row = [f'Responsable du site ', f'{obj.nom_responsable_site}', f'{obj.qualite_responsable_site}', f'{obj.visa_responsable_site}']
            table_data10.append(row)
            
            row = [f'Autre', f'{obj.nom_responsable_autre}', f'{obj.qualite_responsable_autre}', f'{obj.visa_responsable_autre}']
            table_data10.append(row)
            
            row = [f"Permis de feu délivré le: {obj.permis_feu_delivre.strftime('%d/%m/%Y')}", f'', f'', f"Visa du Responsable"]
            table_data0.append(row)
            
            
    # Crer un text
        #paragraph_text = '\n Permis de feu délivré le: {obj.permis_feu_delivre} &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Visa du Responsable'  
        paragraph_text = f"\n\n Permis de feu délivré le: {obj.permis_feu_delivre.strftime('%d/%m/%Y')}         Visa du Responsable"
        
        styles = getSampleStyleSheet()
        para_style = styles["Normal"]

        paragraph = Paragraph(paragraph_text, para_style)
     # Créez le tableau avec les données
        table2 = Table(table_data2, colWidths=[798])
    
        tete = Table(site, colWidths=[399, 399])
        table4 = Table(table_data4, colWidths=[399, 399])
        table6 = Table(table_data6, colWidths=[399, 399])
        table8 = Table(table_data8, colWidths=[399, 399])
        table9 = Table(table_data9, colWidths=[399, 399])
        
        table1 = Table(table_data1 , colWidths=[266 , 266 , 266] )
        table3 = Table(table_data3 , colWidths=[266 , 266 , 266] )
        table5 = Table(table_data5 , colWidths=[266 , 266 , 266] )
        
        table10 = Table(table_data10, colWidths = [222, 192, 192, 192])
        
        table7 = Table(table_data7, colWidths=[319, 80, 319, 80])
        
        vide1 = Table(table_vide1, colWidths=[798])
        fin = Table(table_data0, colWidths = [222, 192, 192, 192])
        
        # table2 = Table(table_data1, colWidths=[400, 400])

        # Définissez le style du tableau, y compris les lignes
        style01 = TableStyle([
            # ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
            ('ALIGN', (0, 0), (0, 0), 'CENTER'),
            ('ALIGN', (1,0), (1,0), 'CENTER'),
            ('ALIGN', (1,0), (1,1), 'CENTER'),
            ('BOTTOMPADDING', (0, 0), (-1, -1), 7),
            ('BOTTOMPADDING', (0, 0), (0, 0), -23),
            # ('FONTNAME', (0,0), (0,0), 'DarkGardenMK'),
            ('FONTNAME', (1,0), (1,0), 'Helvetica-Bold'),
            ('FONTNAME', (1,0), (1,1), 'Helvetica-Bold'),
            ('GRID', (1, 0), (-1, -1), 0.5, colors.black),
            ('BOX', (0,0), (-1,-1), 0.5, colors.black),
        ])
        
        styletete = TableStyle([
            ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
            ('BOTTOMPADDING', (0, 0), (-1, -1), 9),
            ('GRID', (0, 0), (-1, -1), 0.5, colors.black),
            ('BACKGROUND', (0,0), (-1,-1), '#2ecd23'),
            ('FONTNAME', (0,0), (-1,-1), 'Helvetica-Bold'),
        ])
        
        style = TableStyle([
            ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
            ('BOTTOMPADDING', (0, 0), (-1, -1), 9),
            ('GRID', (0, 0), (-1, -1), 0.5, colors.black),
        ])        
        
        style2 = TableStyle([
            ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
            ('BOTTOMPADDING', (0, 0), (-1, -1), 9),
            ('GRID', (0, 0), (-1, -1), 0.5, colors.black),
            ('FONTNAME', (0,0), (-1,-1), 'Helvetica-Bold'),
        ])
        
        style4 = TableStyle([
            ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
            ('BOTTOMPADDING', (0, 0), (-1, -1), 9),
            ('GRID', (0, 0), (-1, -1), 0.5, colors.black),
            ('BACKGROUND', (0,0), (1,0), colors.red),
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
            ('FONTNAME', (0,0), (-1,0), 'Helvetica-Bold'),
        ])
        
        style5 = TableStyle([
            ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
            ('BOTTOMPADDING', (0, 0), (-1, -1), 9),
            ('GRID', (0, 0), (-1, -1), 0.5, colors.black),
            ('BACKGROUND', (0,0), (-1,0), colors.yellow),
            ('FONTNAME', (0,0), (-1,0), 'Helvetica-Bold'),
        ])   
        
        style6 = TableStyle([   
            ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
            ('BOTTOMPADDING', (0, 0), (-1, -1), 9),
            ('GRID', (0, 0), (-1, -1), 0.5, colors.black),
            ('BACKGROUND', (0, 0), (-1, 0), colors.blue),
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.white), 
            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),            
        ])
        
        style7 = TableStyle([   
            ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
            ('BOTTOMPADDING', (0, 0), (-1, -1), 9),
            ('GRID', (0, 0), (-1, -1), 0.5, colors.black),
            ('BACKGROUND', (2, 5), (2, 6), colors.blue),
            ('TEXTCOLOR', (2, 5), (2, 6), colors.white),
            ('FONTNAME', (2, 5), (2, 6), 'Helvetica-Bold'),
            ('FONTNAME', (1, 0), (-1, 0), 'Helvetica-Bold'),
            ('ALIGN', (1, 1), (1, -1), 'CENTER'),
            ('ALIGN', (-1, 1), (-1, -1), 'CENTER'),
        ])
        
        style8 = TableStyle([
            ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
            ('BOTTOMPADDING', (0, 0), (-1, -1), 9),
            ('GRID', (0, 0), (-1, -1), 0.5, colors.black),
            ('BACKGROUND', (0,0), (-1,0), colors.blue),
            ('TEXTCOLOR', (0,0), (-1,0), colors.white),
            ('FONTNAME', (0,0), (-1,0), 'Helvetica-Bold'),
            # ('FONTNAME', (0,1), (0,1), 'Helvetica-Bold'),
        ])        
        
        style9 = TableStyle([
            ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
            ('BOTTOMPADDING', (0, 0), (-1, -1), 9),
            ('GRID', (0, 0), (-1, -1), 0.5, colors.black),
            ('BACKGROUND', (0,0), (-1,0), colors.red),
            ('TEXTCOLOR', (0,0), (-1,0), colors.white),
            ('FONTNAME', (0,0), (-1,0), 'Helvetica-Bold'),
        ])        
        
        style10 = TableStyle([
            ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
            ('BOTTOMPADDING', (0, 0), (-1, -1), 9),
            ('GRID', (0, 0), (-1, -1), 0.5, colors.black),
            ('BACKGROUND', (0,0), (-1,0), '#2ecd23'),
            ('FONTNAME', (0,0), (-1,0), 'Helvetica-Bold'),
        ])          
        
        style0 = TableStyle([
            ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
            ('BOTTOMPADDING', (0, 0), (-1, -1), 9),
            ('TEXTCOLOR', (0,0), (-1,0), colors.blue),  
        ])        
        
        table1.setStyle(style01)
        tete.setStyle(styletete)
        table2.setStyle(style2)
        table3.setStyle(style2)
        table4.setStyle(style4)
        table5.setStyle(style5)
        table6.setStyle(style6)
        table7.setStyle(style7)
        table8.setStyle(style8)
        table9.setStyle(style9)
        fin.setStyle(style0)
        table10.setStyle(style10)
        
        vide1.setStyle(style)

        # Construisez le PDF
        elements = [table1, vide1, tete, table2, table3, vide1, table4, table5, table6, table7, vide1, table8, vide1, table9, table10, fin]
        
        doc.build(elements)

        return response

    generate_pdf.short_description = "Générer un PDF"
    
    
    
'''
PDF ESPACE CONFINEE

            row = ['{} Soudage\n'.format("\u2713" if obj.soudage else "\u2717"), '{} Tronconnage\n'.format("\u2713" if obj.tronconnage else "\u2717") , '{} Decoupage\n'.format("\u2713" if obj.decoupage else "\u2717")  ,'{} Meulage\n'.format("\u2713" if obj.meulage else "\u2717") ,'Autre(s) à préciser \n\n {"[x]" if obj.autre_type_travaux else "[  ]"}',


'''

class PdfEspaceConfine(admin.ModelAdmin):
    actions = ['generate_pdf']
        
    def generate_pdf(self, request, queryset):
        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="formulaire.pdf"'

        # Créez un objet SimpleDocTemplate pour le PDF
        doc = SimpleDocTemplate(response, pagesize=A3)
        
        vide = []
        
        table_data1 = []
        table_data2 = []
        table_data3 = []
        table_data4 = []
        table_data5 = []
        table_data6 = []
        table_data7 = []
        table_data8 = []
        table_data9 = []
        
        table_data10 = []
        table_data11 = []
        table_data12 = []
        table_data13 = []
        table_data14 = []
        table_data15 = []
        
        table_data16 = []
        table_data17 = []
        
        for obj in queryset:
            
            row = [f'']
            vide.append(row)            
            
            row = [logo, f'SGHSSES-TEMP-JOV-904.1',f'Date: {obj.date_entete}']
            table_data1.append(row)
            
            row = [f'', f'PERMIS D’ENTREE EN ESPACE CONFINE',f'Registre: {obj.registre_entete}']
            table_data1.append(row)
            
            row = [f' 1.     DESCRIPTION DU TRAVAIL']
            table_data2.append(row)  
            
            row = [f' Site: {obj.site}', f' Equipement: {obj.equipement}', f' Entreprise intervenante : {obj.entreprise_intervenante}']
            table_data3.append(row)
             
            row = [f" Date de début: {obj.date_debut}",
                   f" Heure de début: {obj.heure_debut}                                Heure de fin: {obj.heure_fin}",
                   f" Date de fin: {obj.date_fin}"]
            table_data4.append(row)
            
            row = [f' Descriptif du travail: \n {obj.descriptif_travail} \n']
            table_data5.append(row)
            
            row = [f"2. PREPARATION DE L'INTERVENTION", f'Requis', f'', f'3. EQUIPEMENT DE SECURITE', f'Requis', f'', f'Type']
            table_data6.append(row)
            
            row = [f'', f'Oui', f'Non', f'', f'Oui', f'Non', f'']
            table_data6.append(row)
            
            row = [f'Consignation électrique', '{}'.format("\u2717" if obj.consignation_electique else ""), '{}'.format("" if obj.consignation_electique else "\u2717"), f'Détecteur de gaz', '{}'.format("\u2717" if obj.detecteur_gaz else ""), '{}'.format("" if obj.detecteur_gaz else "\u2717"), f'{obj.type_detecteur_gaz}']
            table_data6.append(row)
            
            row = [f'Consignation  fluidique ', '{}'.format("\u2717" if obj.consignation_fluidique else ""), '{}'.format("" if obj.consignation_fluidique else "\u2717"), f'Appareil respiratoire autonome ', '{}'.format("\u2717" if obj.appareil_respiratoire_autonome else ""), '{}'.format("" if obj.appareil_respiratoire_autonome else "\u2717"), f'{obj.type_appareil_respiratoire_autonome}']
            table_data6.append(row)
            
            row = [f'Consignation mécanique ', '{}'.format("\u2717" if obj.consignation_mecanique else ""), '{}'.format("" if obj.consignation_mecanique else "\u2717"), f'Appareil respiratoire isolant ', '{}'.format("\u2717" if obj.appareil_respiratoire_isolant else ""), '{}'.format("" if obj.appareil_respiratoire_isolant else "\u2717"), f'{obj.type_appareil_respiratoire_isolant}']
            table_data6.append(row)
            
            row = [f'Ventilation ', '{}'.format("\u2717" if obj.ventilation else ""), '{}'.format("" if obj.ventilation else "\u2717"), f'Masque filtrant ', '{}'.format("\u2717" if obj.masque else ""), '{}'.format("" if obj.masque else "\u2717"), f'{obj.type_masque}']
            table_data6.append(row)
            
            row = [f'Ventilation forcée', '{}'.format("\u2717" if obj.ventilation_forcee else ""), '{}'.format("" if obj.ventilation_forcee else "\u2717"), f'Harnais de sécurité ', '{}'.format("\u2717" if obj.harnais else ""), '{}'.format("" if obj.harnais else "\u2717"), f'{obj.type_harnais}']
            table_data6.append(row)
            
            row = [f"Plan d’urgence ", '{}'.format("\u2717" if obj.plan_urgence else ""), '{}'.format("" if obj.plan_urgence else "\u2717"), f'Treuil et protection antichute', '{}'.format("\u2717" if obj.treuil else ""), '{}'.format("" if obj.treuil else "\u2717"), f'{obj.type_treuil}']
            table_data6.append(row)
            
            row = [f'ASET', '{}'.format("\u2717" if obj.ASET else ""), '{}'.format("" if obj.ASET else "\u2717"), f'Corde assurance', '{}'.format("\u2717" if obj.corde_assurance else ""), '{}'.format("" if obj.corde_assurance else "\u2717"), f'{obj.type_corde_assurance}']
            table_data6.append(row)
            
            row = [f'*Autre préparation à préciser :', f'', f'', f'Panneaux  de signalisation', '{}'.format("\u2717" if obj.panneaux else ""), '{}'.format("" if obj.panneaux else "\u2717"), f'{obj.type_panneaux}']
            table_data6.append(row)
            
            row = [f'{obj.autre_intervention}', f'', f'', f'Balisage de sécurité', '{}'.format("\u2717" if obj.balisage else ""), '{}'.format("" if obj.balisage else "\u2717"), f'{obj.type_balisage}']
            table_data6.append(row)
            
            row = [f'', f'', f'', f'*Moyen de communication surveillant&intervenant(s) à préciser : \n {obj.moyen_intervenant}', f'',f'', f'']
            table_data6.append(row)
            
            row = [f"4. QUALITE DE L'AIR"]
            table_data7.append(row)
            
            row = [f'Substance', f'Applicable', f'Date', f'Heure', f'PPM/%', f'Heure', f'PPM/%', f'Heure', f'PPM/%', f'Limites']
            table_data8.append(row) 
            
            row = [f'O2', '{}'.format("\u2713" if obj.o2_applicable else ""), obj.o2_date.strftime('%d/%m/%Y'), obj.o2_heure1.strftime('%H:%M') , obj.o2_PPM1, obj.o2_heure2.strftime('%H:%M'), obj.o2_PPM2, obj.o2_heure3.strftime('%H:%M'), obj.o2_PPM3, f'19,5 – 21.5%']
            table_data8.append(row) 
            
            row = [f'% LIE', '{}'.format("\u2713" if obj.LIE_applicable else ""), obj.LIE_date.strftime('%d/%m/%Y'), obj.LIE_heure1.strftime('%H:%M'), obj.LIE_PPM1, obj.LIE_heure2.strftime('%H:%M'), obj.LIE_PPM2, obj.LIE_heure3.strftime('%H:%M'), obj.LIE_PPM3, f'<5 %']
            table_data8.append(row) 
            
            row = [f'CO', '{}'.format("\u2713" if obj.Co_applicable else ""), obj.Co_date.strftime('%d/%m/%Y'), obj.Co_heure1.strftime('%H:%M'), obj.Co_PPM1, obj.Co_heure2.strftime('%H:%M'), obj.Co_PPM2, obj.Co_heure3.strftime('%H:%M'), obj.Co_PPM3, f'<35 ppm']
            table_data8.append(row) 
            
            row = [f'SO2', '{}'.format("\u2713" if obj.SO_applicable else ""), obj.SO_date.strftime('%d/%m/%Y'), obj.SO_heure1.strftime('%H:%M'), obj.SO_PPM1, obj.SO_heure2.strftime('%H:%M'), obj.SO_PPM2, obj.SO_heure3.strftime('%H:%M'), obj.SO_PPM3, f'<2 ppm']
            table_data8.append(row) 
            
            row = [f'H2S', '{}'.format("\u2713" if obj.H2S_applicable else ""), obj.H2S_date.strftime('%d/%m/%Y'), obj.H2S_heure1.strftime('%H:%M'), obj.H2S_PPM1, obj.H2S_heure2.strftime('%H:%M'), obj.H2S_PPM2, obj.H2S_heure3.strftime('%H:%M'), obj.H2S_PPM3, f'<10 ppm']
            table_data8.append(row) 
            
            row = [f'NH3', '{}'.format("\u2713" if obj.NH3_applicable else ""), obj.NH3_date.strftime('%d/%m/%Y'), obj.NH3_heure1.strftime('%H:%M'), obj.NH3_PPM1, obj.NH3_heure2.strftime('%H:%M'), obj.NH3_PPM2, obj.NH3_heure3.strftime('%H:%M'), obj.NH3_PPM3, f'<5 ppm']
            table_data8.append(row)            
            
            row = [f'Nom du testeur de gaz: {obj.nom_testeur} ', f'Signature:']
            table_data9.append(row)
            
            row = [f'5. AUTORISATION (Responsable Jovena)']
            table_data10.append(row)
            
            row = [f'Nom: {obj.nom_reponsable_jovena} \n \n', f"Date / heure:       {obj.date_heure1.strftime('%d/%m/%Y      à      %H:%M')} \n \n" , f'Signature \n \n' ]
            table_data11.append(row)
            
            row = [f"6. SURVEILLANT DE L’ESPACE CONFINE"]
            table_data12.append(row)
            
            row = [f'Nom: {obj.nom_surveillant} \n \n', f"Date / heure:       {obj.date_heure2.strftime('%d/%m/%Y      à      %H:%M')} \n \n" , f'Signature \n \n']
            table_data13.append(row)
            
            row = [f"7. CLOTURE DU PERMIS (Responsable habilité de l’entreprise intervenante)"]
            table_data14.append(row)
            
            row = [f'Nom: {obj.nom_cloture} \n \n', f"Date / heure:       {obj.date_heure3.strftime('%d/%m/%Y      à      %H:%M')} \n \n" , f'Signature \n \n']
            table_data15.append(row)
            
            row = [f'ALERTE EN CAS D’INCIDENT', f'NUMEROS D’URGENCE']
            table_data16.append(row)
            
            row = [f'', f'Pompiers:  {obj.pompier}']
            table_data16.append(row)
            
            row = [f'', f'Ambulance:  {obj.ambulance}']
            table_data16.append(row)
            
            row = [f'', f'Responsable du site:  {obj.responsable_site}']
            table_data16.append(row)
            
            row = [f'', f'Responsable Jovena:  {obj.responsable_jovena}']
            table_data16.append(row)
            
            row = [f'Permis délivré le:  {obj.permi_delivre}', f'Visa du Responsable Jovena']
            table_data17.append(row)
            
        vide1 = Table(vide , colWidths=[798])
        
        table1 = Table(table_data1 , colWidths=[266 , 266 , 266])
        table2 = Table(table_data2 , colWidths=[798])
        table3 = Table(table_data3 , colWidths=[266 , 266 , 266])
        table4 = Table(table_data4 , colWidths=[240 , 318 , 240])
        table5 = Table(table_data5 , colWidths=[798])
        table6 = Table(table_data6 , colWidths=[323, 38, 38, 224, 38,38, 99])
        table7 = Table(table_data7 , colWidths=[798])
        table8 = Table(table_data8 , colWidths=[99, 75, 75, 75, 75, 75, 75, 75, 75, 99])
        table9 = Table(table_data9 , colWidths=[549, 249])
        
        table10 = Table(table_data10 , colWidths=[798])
        table11 = Table(table_data11 , colWidths=[266 , 266 , 266])
        table12 = Table(table_data12 , colWidths=[798])
        table13 = Table(table_data13 , colWidths=[266 , 266 , 266])
        table14 = Table(table_data14 , colWidths=[798])
        table15 = Table(table_data15 , colWidths=[266 , 266 , 266])
        
        table16 = Table(table_data16 , colWidths=[399, 399])
        table17 = Table(table_data17 , colWidths=[399, 399])
       
        styleVide = TableStyle([
       ])
       
        style1 = TableStyle([
            # ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
            ('ALIGN', (0, 0), (0, 0), 'CENTER'),
            ('ALIGN', (1,0), (1,0), 'CENTER'),
            ('ALIGN', (1,0), (1,1), 'CENTER'),
            ('BOTTOMPADDING', (0, 0), (-1, -1), 7),
            ('BOTTOMPADDING', (0, 0), (0, 0), -23),
            # ('FONTNAME', (0,0), (0,0), 'DarkGardenMK'),
            ('FONTNAME', (1,0), (1,0), 'Helvetica-Bold'),
            ('FONTNAME', (1,0), (1,1), 'Helvetica-Bold'),
            ('GRID', (1, 0), (-1, -1), 0.5, colors.black),
            ('BOX', (0,0), (-1,-1), 0.5, colors.black),
        ])
        
        style2 = TableStyle([
            ('FONTNAME', (0,0), (-1,0), 'Helvetica-Bold'),
            ('BACKGROUND', (0,0), (-1,0), '#2ecd23'),
            ('GRID', (0, 0), (-1, -1), 0.5, colors.black),
        ])
        
        style3 = TableStyle([
            ('GRID', (0, 0), (-1, -1), 0.5, colors.black),
        ])
        
        style6 = TableStyle([
            ('BOX', (0,0), (0,1), 0.5, colors.black),
            ('BOX', (3,0), (3,1), 0.5, colors.black),
            ('BOX', (1,0), (2,0), 0.5, colors.black),
            ('BOX', (4,0), (5,0), 0.5, colors.black),
            ('BOX', (0,9), (2,-1), 0.5, colors.black),
            ('BOX', (3,11), (-1,-1), 0.5, colors.black),
            
            ('GRID', (1,1), (2,1), 0.5, colors.black),
            ('GRID', (4,1), (5,1), 0.5, colors.black),
            ('GRID', (0,2), (-1,8), 0.5, colors.black),
            ('GRID', (3,9), (-1,10), 0.5, colors.black),
            
            ('BOTTOMPADDING', (0,0), (0,0), -5),
            ('FONTSIZE', (0,0),(0,0), 12),
            ('BOTTOMPADDING', (3,0), (3,0), -5),
            ('FONTSIZE', (3,0),(3,0), 12),
            ('BOTTOMPADDING', (-1,0), (-1,0), -5),
            ('RIGHTPADDING', (1,0), (1,0), -28),
            ('RIGHTPADDING', (4,0), (4,0), -28),
            ('ALIGN', (0,0), (6,1), 'CENTER'),
            ('ALIGN', (1,2), (2,8), 'CENTER'),
            ('ALIGN', (4,2), (5,10), 'CENTER'),
            ('BACKGROUND', (0,0), (2,1), colors.red),
            ('BACKGROUND', (3,0), (6,1), colors.blue),
            ('TEXTCOLOR', (0,0), (6,1), colors.white),
            ('FONTNAME', (0,0), (6,1), 'Helvetica-Bold'),
        ])
        
        style7 = TableStyle([
            ('GRID', (0, 0), (-1, -1), 0.5, colors.black),
            ('BACKGROUND', (0,0), (-1,-1), '#c7c7c7'),
            ('FONTNAME', (0,0), (-1,-1), 'Helvetica-Bold'),
        ])
        
        style8 = TableStyle([
            ('GRID', (0, 0), (-1, -1), 0.5, colors.black),
            ('ALIGN', (0,0), (-1,-1), 'CENTER'),
            ('BACKGROUND', (-1,0), (-1,-1), '#cfcfcf'),
            ('FONTNAME', (-1,0), (-1,-1), 'Helvetica-Bold'),
            ('FONTNAME', (0,0), (-1,0), 'Helvetica-Bold'),
            ('FONTNAME', (0,0), (0,-1), 'Helvetica-Bold'),
            ('TEXTCOLOR', (1,1), (1,-1), colors.green),
        ])
        
        style9 = TableStyle([
            ('BOX', (0, 0), (-1, -1), 0.5, colors.black),
            ('FONTNAME', (0,0), (-1,-1), 'Helvetica-Bold'),
        ])
        
        style16 = TableStyle([
            ('GRID', (0, 0), (-1,0), 0.5, colors.black),
            ('FONTNAME', (0,0), (-1,0), 'Helvetica-Bold'),
            ('BACKGROUND', (0,0), (-1,0), colors.red ),
            ('TEXTCOLOR', (0,0), (-1,0), colors.white),
            ('BOX', (0,1), (0,-1), 0.5, colors.black),
            ('BOX', (1,1), (1,-1), 0.5,colors.black),
        ])
        
        style17 = TableStyle([
            ('TEXTCOLOR', (0,0), (-1,-1), '#0566e6'),
            ('BOTTOMPADDING', (0,0), (-1,-1), -28),
        ])
        
        table1.setStyle(style1)
        table2.setStyle(style2)
        table3.setStyle(style3)
        table4.setStyle(style3)
        table5.setStyle(style3)
        table6.setStyle(style6)
        table7.setStyle(style7)
        table8.setStyle(style8)
        table9.setStyle(style9)
        
        table10.setStyle(style7)
        table11.setStyle(style3)
        table12.setStyle(style7)
        table13.setStyle(style3)
        table14.setStyle(style7)
        table15.setStyle(style3)
        
        table16.setStyle(style16)
        table17.setStyle(style17)
        
        vide1.setStyle(styleVide)

        elements = [table1, vide1, table2, table3, table4, table5, table6, table7, table8, table9, table10, table11, table12, table13, table14, table15, table16, table17]
        #elements.append(paragraph)
        
        doc.build(elements)

        return response

    generate_pdf.short_description = "Générer un PDF"



"""
PDF CHECKLIST EXCAVATION
"""

class PdfExcavation(admin.ModelAdmin):
    actions = ['generate_pdf']
        
    def generate_pdf(self, request, queryset):
        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="formulaire.pdf"'

        # Créez un objet SimpleDocTemplate pour le PDF
        doc = SimpleDocTemplate(response, pagesize=A3)
        
        vide = []
        tete = []
        
        table_data1 = []
        table_data2 = []
        table_data3 = []
        table_data4 = []
        table_data5 = []
        table_data6 = []
        table_data7 = []
        table_data8 = []
        table_data9 = []
        
        table_data10 = []
        table_data11 = []
        table_data12 = []
        table_data13 = []
        table_data14 = []
        table_data15 = []
        table_data16 = []
        table_data17 = []
        table_data18 = []
        table_data19 = []
        table_data20 = []
        table_data21 = []
        table_data22 = []
        table_data23 = []
        table_data24 = []
        table_data25 = []
        
        
        for obj in queryset:
            
            row = [f'']
            vide.append(row)
            
            row = [logo, f'SGHSSES-PRO-JOV—905.1',f'Date: {obj.date_entete}']
            tete.append(row)
            
            row = [f'', f'PERMIS D’ EXCAVATION ',f'Registre: {obj.Registre_entete}']
            tete.append(row)
            
            row = [f'Site :   {obj.site}', f'Client :  {obj.client}']
            table_data1.append(row)
            
            row = [f'Localité :   {obj.localite}', f'Entreprise intervenante :  {obj.entreprise_intervenante}']
            table_data1.append(row)
            
            row = [f'DESCRIPTIF DU TRAVAIL: \n {obj.descriptif}']
            table_data2.append(row)
            
            row = [f'Profondeur et longueur de l’excavation :   {obj.profondeur_excavation}', f'Zone :  {obj.zone}']
            table_data3.append(row)
            
            row = [f'Type d’excavation ', f'Mécanique', f'Manuelle', f'Autre à préciser ']
            table_data4.append(row)
            
            row = [f'LISTE DE DESSINS:', obj.dessin1, obj.dessin2, obj.dessin3, obj.dessin4]
            table_data5.append(row)
            
            row = [f'Note: les dessins listes doivent être attachés à ce permis']
            table_data6.append(row)
            
            row = [f'OBSTRUCTIONS SOUTERRAINES', f'COMMENTAIRE / DETECTE']
            table_data7.append(row) 
            
            row = [f'Lignes d’eau', '{} Eau incendie'.format("\u2713" if obj.eau_incendie else "\u2717"), '{} Eau de rivière'.format("\u2713" if obj.eau_riviere else "\u2717"), '{} Eau domestique'.format("\u2713" if obj.eau_domestique else "\u2717"), obj.commentaire_obstruction1]
            table_data8.append(row)
            
            row = [f'Egout ', '{} Eaux pluviales'.format("\u2713" if obj.eau_pluviale else "\u2717"), '{} Effluents'.format("\u2713" if obj.effluent else "\u2717"), '{} Sanitaires'.format("\u2713" if obj.sanitaire else "\u2717"), obj.commentaire_obstruction2]
            table_data8.append(row)
            
            row = ['{} Câble de communication'.format("\u2713" if obj.cable_communication else "\u2717"), '{} câble cathodique'.format("\u2713" if obj.cable_cathodique else "\u2717"), obj.commentaire_obstruction3]
            table_data9.append(row)
            
            row = ['{} mise à la terre'.format("\u2713" if obj.mise_terre else "\u2717"), '{} ligne de gaz'.format("\u2713" if obj.ligne_gaz else "\u2717"), obj.commentaire_obstruction4]
            table_data9.append(row)
            
            row = ['{} structure adjacente'.format("\u2713" if obj.structure_adjacente else "\u2717"), '{} autre (à préciser)'.format("\u2713" if obj.atre_obstruction else "\u2717"), obj.commentaire_obstruction5]
            table_data9.append(row)
            
            row = [f'ELECTRIQUE', '{} | 11 KV'.format("\u2713" if obj.electrique_11kv else "\u2717"), '{} | 6.6 KV'.format("\u2713" if obj.electrique_6kv else "\u2717"),
                   '{} | 690 V'.format("\u2713" if obj.electrique_690v else "\u2717"), '{} | < 690 V'.format("\u2713" if obj.electrique_690i else "\u2717"), obj.commentaire_obstruction6]
            table_data10.append(row)
            
            row = [f'CONSIDERATIONS SPECIFIQUES', f'COMMENTAIRE']
            table_data11.append(row)
            
            row = ['{} PENTE'.format("\u2713" if obj.pente else "\u2717"), '{} BANC'.format("\u2713" if obj.banc else "\u2717"), '{} ETAYAGE'.format("\u2713" if obj.etayage else "\u2717"), obj.commentaire1]
            table_data12.append(row)
            
            row = ['{} PROTECTION DE NUIT'.format("\u2713" if obj.pretection_nuit else "\u2717"), '{} PROTECTION DES OUVERTURES (BARRICADE)'.format("\u2713" if obj.pretection_ouverture else "\u2717"), obj.commentaire2]   
            table_data13.append(row)
            
            row = ["{} PERMIS D'ENTREE EN ESPACE CONFINE".format("\u2713" if obj.permis_espace else "\u2717"), "{} POMPAGE D'EAU".format("\u2713" if obj.pompage_eau else "\u2717"), obj.commentaire3]   
            table_data13.append(row)
            
            row = ['{} FERMETURE DE ROUTE'.format("\u2713" if obj.fermeture_route else "\u2717"), f'', obj.commentaire4]   
            table_data13.append(row)
            
            row = [f'MESURE DE SECURITE ADDITIONNELLE (A PRECISER) :  {obj.mesure_securite_additionnel}']
            table_data14.append(row)
            
            row = [f'DETECTION DES STRUCTURES ET SERVICES NON-APPARENTS']
            table_data15.append(row)
            
            row = [format("\u2713 \n" if obj.effectuee else "\u2717 \n"), f'EFFECTUEE \n', f'PAR \n', f'NOM: {obj.effectuer_nom} \n', f"DATE: {obj.effectuer_date.strftime('%d/%m/%Y')} \n", f'SIGNATURE \n']
            table_data16.append(row)
            
            row = [format("\u2713 \n" if obj.representant_contracant else "\u2717 \n"), f'REPRESENTANT \n CONTRACTANT', f'PAR \n', f'NOM: {obj.representant_contracant_nom} \n', f"DATE: {obj.representant_contracant_date.strftime('%d/%m/%Y')} \n", f'SIGNATURE \n']
            table_data16.append(row)
            
            row = [f'APPROBATION']
            table_data17.append(row)
            
            row = [f'SUPERVISEUR DES DESSINATEURS \n', f'NOM: {obj.superviseur_nom} \n', f'DATE: {obj.superviseur_date.strftime("%d/%m/%Y")} \n', f'SIGNATURE \n']
            table_data18.append(row)
            
            row = [f'REPRESENTANT DU PROPRIETAIRE \n', f'NOM: {obj.representant_proprietaire_nom} \n', f'DATE: {obj.representant_proprietaire_date.strftime("%d/%m/%Y")} \n', f'SIGNATURE \n']
            table_data18.append(row)
            
            row = [f'ACCORD']
            table_data19.append(row)
            
            row = [f"JE COMPRENDS LA NATURE ET L'ETENDUE DES TRAVAUX ET JE ME CONFORMERAI A TOUTES LES CONDITIONS ET LES PRECAUTIONS \n A SUIVRE POUR ACHEVER LE TRAVAIL"]
            table_data20.append(row)
            
            row = [f"SUPERVISEUR D'EXCAVATION \n", f'NOM: {obj.superviseur_excavation_nom} \n', f'DATE: {obj.superviseur_excavation_date.strftime("%d/%m/%Y")} \n', f'SIGNATURE \n']
            table_data21.append(row)
            
            row = [f"ACHEVEMENT DE L'EXCAVATION"]
            table_data22.append(row)
            
            row = ["A LA FIN DES TRAVAUX, LE SUPERVISEUR D'EXCAVATION SIGNERA EN DESSOUS ET INDIQUERA LA DATE D'ACHEVEMENT DES TRAVAUX PUIS ENVERRA \n AU SUPERVISEUR DES DESSINATEURS ACCOMPAGNES DES DESSINS TOUTES MODIFICATIONS/ADDITIONS OU SUPPRESSIONS."]
            table_data23.append(row)
            
            row = ["SUPERVISEUR D'EXCAVATION", f"DATE D'ACHEVEMENT DES TRAVAUX \n D'EXCAVATION: {obj.date_achevement_excavation}", f'SIGNATURE \n']
            table_data24.append(row)
            
            row = [f'Permis d’excavation délivré le : {obj.permis_excavation_delivre.strftime("%d/%m/%Y")}', f'Visa du Responsable ']
            table_data25.append(row)
            
        vide = Table(vide, colWidths = [798])
        entete = Table(tete , colWidths=[266 , 266 , 266])
        
        table1 = Table(table_data1, colWidths=[399, 399])
        table2 = Table(table_data2, colWidths=[798])
        table3 = Table(table_data3, colWidths=[399, 399])
        table4 = Table(table_data4, colWidths=[201, 199, 199, 199])
        table5 = Table(table_data5, colWidths=[162, 159, 159, 159, 159])
        table6 = Table(table_data6, colWidths=[798])
        table7 = Table(table_data7, colWidths=[628, 170])
        table8 = Table(table_data8, colWidths=[157, 157, 157, 157, 170])
        table9 = Table(table_data9, colWidths=[314, 314, 170])
        
        table10 = Table(table_data10, colWidths=[128, 125, 125, 125, 125, 170])
        table11 = Table(table_data11, colWidths=[628, 170])
        table12 = Table(table_data12, colWidths=[209,210,209, 170])
        table13 = Table(table_data13, colWidths=[314, 314, 170])
        table14 = Table(table_data14, colWidths=[798])
        table15 = Table(table_data15, colWidths=[798])
        table16 = Table(table_data16, colWidths=[22, 150, 45, 310, 92, 178])
        table17 = Table(table_data17, colWidths=[798])
        table18 = Table(table_data18, colWidths=[217, 310, 92, 178])
        table19 = Table(table_data19, colWidths=[798])
        table20 = Table(table_data20, colWidths=[798])
        table21 = Table(table_data21, colWidths=[217, 310, 92, 178])
        table22 = Table(table_data22, colWidths=[798])
        table23 = Table(table_data23, colWidths=[798])
        table24 = Table(table_data24, colWidths=[217, 310, 270])
        table25 = Table(table_data25, colWidths=[628, 170])
        
        
        styleVide = [
        ]
        
        styletete = TableStyle([
            # ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
            ('ALIGN', (0, 0), (0, 0), 'CENTER'),
            ('ALIGN', (1,0), (1,0), 'CENTER'),
            ('ALIGN', (1,0), (1,1), 'CENTER'),
            ('BOTTOMPADDING', (0, 0), (-1, -1), 7),
            ('BOTTOMPADDING', (0, 0), (0, 0), -23),
            # ('FONTNAME', (0,0), (0,0), 'DarkGardenMK'),
            ('FONTNAME', (1,0), (1,0), 'Helvetica-Bold'),
            ('FONTNAME', (1,0), (1,1), 'Helvetica-Bold'),
            ('GRID', (1, 0), (-1, -1), 0.5, colors.black),
            ('BOX', (0,0), (-1,-1), 0.5, colors.black),
        ])
        
        styleGrid = TableStyle([
            ('GRID', (0,0), (-1,-1), 0.5, colors.black),
        ])
        
        style1 = TableStyle([
            ('GRID', (0,0), (-1,-1), 0.5, colors.black),
            ('BACKGROUND', (0,0), (-1,-1), '#2ecd23'),
        ])
        
        style5 = TableStyle([
            ('GRID', (0,0), (-1,-1), 0.5, colors.black),
            ('BACKGROUND', (0,0), (0,0), '#bdbdbd'),
            ('FONTNAME', (0,0), (0,0), 'Helvetica-Bold'),
        ])
        
        style6 = TableStyle([
            ('GRID', (0,0), (-1,-1), 0.5, colors.black),
            ('TEXTCOLOR', (0,0), (-1,-1), colors.red),
            ('FONTNAME', (0,0), (-1,-1), 'Times-Roman'),
            ('ALIGN', (0,0), (-1,-1), 'CENTER'),
            ('FONTSIZE', (0,0), (-1,-1), 14),
            ('BOTTOMPADDING', (0,0), (-1,-1), 7),
        ])
        
        style7 = TableStyle([
            ('GRID', (0,0), (-1,-1), 0.5, colors.black),
            ('BACKGROUND', (0,0), (-1,-1), '#bdbdbd'),
            ('FONTNAME', (0,0), (-1,-1), 'Helvetica-Bold'),
            ('ALIGN', (0,0), (-1,-1), 'CENTER'),
        ])
        
        style8 = TableStyle([
            ('GRID', (0,0), (-1,-1), 0.5, colors.black),
            ('ALIGN', (0,0), (-1,-1), 'CENTER'),
            ('FONTNAME', (0,0), (0,1), 'Helvetica-Bold'),
        ])
        
        style12 = TableStyle([
            ('GRID', (0,0), (-1,-1), 0.5, colors.black),
            ('ALIGN', (0,0), (-1,-1), 'CENTER'),
        ])
        
        style9 = TableStyle([
            ('GRID', (0,0), (-1,-1), 0.5, colors.black),
            ('ALIGN', (0,0), (-1,-1), 'CENTER'),
            ('BACKGROUND', (0,0), (-1,-1), '#f0f0f0'),
        ])
        
        style15 = TableStyle([
            ('GRID', (0,0), (-1,-1), 0.5, colors.black),
            ('BACKGROUND', (0,0), (-1,-1), '#bdbdbd'),
            ('FONTNAME', (0,0), (-1,-1), 'Helvetica-Bold'),
        ])
        
        style16 = TableStyle([
            ('GRID', (4,0), (-1,-1), 0.5, colors.black),
            ('BOX', (0,0), (3,0), 0.5, colors.black),
            ('BOX', (0,1), (3,1), 0.5, colors.black),
            ('ALIGN', (0,0), (2,1), 'CENTER'),
            ('FONTNAME', (0,0), (2,1), 'Helvetica-Bold'),
            ('BOTTOMPADDING', (0,0), (2,0), -2),
            ('BOTTOMPADDING', (0,1), (0,1), -2),
            ('BOTTOMPADDING', (2,1), (2,1), -2),
            ('BACKGROUND', (0,0), (-1,-1), '#2ecd23'),
        ])
        
        style18 = TableStyle([
            ('GRID', (0,0), (-1,-1), 0.5, colors.black),
            ('FONTNAME', (0,0), (0,1), 'Helvetica-Bold'),
            ('BOTTOMPADDING', (0,0), (0,1), -2),
            ('ALIGN', (0,0), (0,1), 'CENTER'),
        ])
        
        style20 = TableStyle([
            ('GRID', (0,0), (-1,-1), 0.5, colors.black),
            ('BACKGROUND', (0,0), (-1,-1), colors.red),
            ('ALIGN', (0,0), (-1,-1), 'CENTER'),
            ('TEXTCOLOR', (0,0), (-1,-1), colors.white),
            ('FONTNAME', (0,0), (-1,-1), 'Helvetica-Bold'),
        ])
        
        style24 = TableStyle([
            ('GRID', (0,0), (-1,-1), 0.5, colors.black),
            ('BOTTOMPADDING', (0,0), (0,0), 12),
            ('ALIGN', (0,0), (0,0), 'CENTER'),
            ('FONTNAME', (0,0), (0,0), 'Helvetica-Bold'),
        ])
        
        style23 = TableStyle([
            ('GRID', (0,0), (-1,-1), 0.5, colors.black),
            ('ALIGN', (0,0), (-1,-1), 'CENTER'),
            ('FONTNAME', (0,0), (-1,-1), 'Helvetica'),
            ('BACKGROUND', (0,0), (-1,-1), colors.whitesmoke),
        ])
        
        style25 = TableStyle([
            #('TEXTCOLOR', (0,0), (-1,-1), '#0566e6'),
            ('TEXTCOLOR', (0,0), (-1,-1), 'LINEARGRADIEN(rgb(255,215,12))'),
            ('BOTTOMPADDING', (0,0), (-1,-1), -28),
        ])
        
        
        vide.setStyle(styleVide)
        entete.setStyle(styletete)
        
        table1.setStyle(style1)
        table2.setStyle(styleGrid)
        table3.setStyle(styleGrid)
        table4.setStyle(styleGrid)
        table5.setStyle(style5)
        table6.setStyle(style6)
        table7.setStyle(style7)
        table8.setStyle(style8)
        table9.setStyle(style9)
        
        table10.setStyle(style8)
        table11.setStyle(style7)
        table12.setStyle(style12)
        table13.setStyle(style9)
        table14.setStyle(styleGrid)
        table15.setStyle(style15)
        table16.setStyle(style16)
        table17.setStyle(style15)
        table18.setStyle(style18)
        table19.setStyle(style15)
        table20.setStyle(style20)
        table21.setStyle(style18)
        table22.setStyle(style15)
        table23.setStyle(style23)
        table24.setStyle(style24)
        table25.setStyle(style25)

        
        elements = [entete, vide, table1, table2, table3, vide, table4, table5, table6, table7, table8, table9, table10, table11, table12, table13, table14, table15, table16, table17, table18, table19, table20, table21, table22, table23, table24, table25]
        
        doc.build(elements)
        
        return response
    
    generate_pdf.short_description = "Générer un PDF"
    

class FrontExcavation(admin.ModelAdmin):
    list_display = ('site', 'localite', 'client', 'entreprise_intervenante' )
    

# class PdfExcavationInlines(admin.TabularInline):
#     model = PdfExcavation
    
# class FrontExcavationInlines(admin.TabularInline):
#     model = FrontExcavation


# class ExcavationAdmin(admin.ModelAdmin):
#     inlines = [PdfExcavationInlines, FrontExcavationInlines]
        
        
# class KPIAdmin(admin.ModelAdmin):
#     list_display = ('name', 'date', 'taux_frequence_incident', 'taux_gravite_incident')  # Remplacez 'field1', 'field2', 'field3' par les champs que vous souhaitez afficher.
#     list_display_links = ('name')  # Définissez les champs que vous souhaitez rendre cliquables.

admin.site.register(KPI_jovena)
admin.site.register(KPI_prestataire)
admin.site.register(KPI_station_service)
admin.site.register(KPI_transporteur)        
    

    
admin.site.unregister(User)
admin.site.register(User , AccountsUserAdmin)

# class Document_jov_admin(admin.ModelAdmin):
#     list_display =('info_trans',)
#     list_display_links = ('info_trans',)
    
# class Document_prest_admin(admin.ModelAdmin):
#     list_display =('info_prest',)
#     list_display_links = ('info_prest',)
    
# class Document_stat_admin(admin.ModelAdmin):
#     list_display =('info_stat',)
#     list_display_links = ('info_stat',)
    
# class Document_trans_admin(admin.ModelAdmin):
#     list_display =('info_trans',)
#     list_display_links = ('info_trans',)


# class DocumentAdminSite(AdminSite):
#     site_header = 'Gestion des Documents'  # Vous pouvez personnaliser le titre du menu DOCUMENT ici

admin.site.register(document_jov)
admin.site.register(document_prest) 
admin.site.register(document_stat)
admin.site.register(document_trans)

# document_admin_site = DocumentAdminSite(name='document_admin')
# document_admin_site.register(document_jov, Document_jov_admin)
# document_admin_site.register(document_prest, Document_prest_admin)
# document_admin_site.register(document_stat, Document_stat_admin)
# document_admin_site.register(document_trans, Document_trans_admin)



admin.site.register(Checklist_stat, ChecklistStatAdmin)
admin.site.register(checklist_permis_feu_prest, ChecklistPermisFeu)

admin.site.register(checklist_excavation, PdfExcavation)
# admin.site.register(FrontExcavation)

admin.site.register(checklist_espace_confinez, PdfEspaceConfine)
