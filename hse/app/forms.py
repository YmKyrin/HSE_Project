from django import forms
from .models import *

class Checklist_statForm(forms.ModelForm):
    class Meta:
        model = Checklist_stat
        
        reponse = forms.ChoiceField(
            widget=forms.RadioSelect,
            choices=[('oui', 'Oui'),
                     ('n/a', 'N/A')
                ],
        )
        
        reponse2 = forms.ChoiceField(
            widget=forms.RadioSelect,
            choices=[('total', 'Total'),
                     ('partiel', 'Partiel')
                ],
        )
        
        fields = '__all__'  
        
    # widgets = {
    #         'charge_station_service': forms.RadioSelect(),
    #         'arret_distribution_total': forms.RadioSelect(),
    #     }
        

class checklist_permis_feu_prestForm(forms.ModelForm):
    class Meta:
        model = checklist_permis_feu_prest      
        
        reponse = forms.ChoiceField(
        widget=forms.RadioSelect,
        choices=[('non', 'NON'), 
                 ('oui', 'OUI'), 
                 ('fait', 'FAIT')
            ],
            
        )
          
        fields = '__all__'
        
    # def __init__(self, *args, **kwargs):
    #     super(checklist_permis_feu_prestForm, self).__init__(*args, **kwargs)
    #     # Formattez le champ heure_debut pour afficher hh:mm sans les secondes
    #     self.fields['heure_debut'].widget.format = '%H:%M'
    # widgets = {
    #     'evacuation_substance': forms.RadioSelect(),
    # }
        
class checklist_permis_excavation_prestForm(forms.ModelForm):
    class Meta:
        model = checklist_excavation
        
        reponse = forms.ChoiceField(
        widget=forms.RadioSelect,
        choices=[('mecanique', 'MECANIQUE'), 
                 ('manuelle', 'MANUELLE'), 
                 ('autre', 'AUTRE')
                ],
            )
        
        fields = '__all__'
        
class checklist_espace_confineForm(forms.ModelForm):
    class Meta:
        model = checklist_espace_confinez
        
        reponse = forms.ChoiceField(
            widget=forms.RadioSelect,
            choices=[('oui','OUI'),
                     ('non','NON')
                    ],
            )
        
        fields = '__all__'

class KPI_jovenaForm(forms.ModelForm):
    class Meta:
        model = KPI_jovena
        
        exclude = ['taux_frequence_incident', 'taux_gravite_incident']
        
class KPI_prestataireForm(forms.ModelForm):
    class Meta:
        model = KPI_prestataire
        
        exclude = ['taux_frequence_incident', 'taux_gravite_incident']

class KPI_station_serviceForm(forms.ModelForm):
    class Meta:
        model = KPI_station_service
        
        exclude = ['taux_frequence_incident', 'taux_gravite_incident']

class KPI_transporteurForm(forms.ModelForm):
    class Meta:
        model = KPI_transporteur
        
        exclude = ['taux_frequence_incident', 'taux_gravite_incident']