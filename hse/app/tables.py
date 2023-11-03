import django_tables2 as tables
from .models import Person, Performance_sante

class PersonTable(tables.Table):
    class Meta:
        model = Person
        

class PerformanceTable(tables.Table):
    
    heure_travailler = tables.Column()
    accident = tables.Column()
    poste_adapte = tables.Column()
    soins_medicaux = tables.Column()
    premier_secours = tables.Column()
    presque_accident = tables.Column()
    
    total = tables.Column(verbose_name='Total', orderable=False, empty_values=())
    
    
    def render_total(self, record):
        return (record.accident + record.poste_adapte + record.soins_medicaux + record.premier_secours + record.presque_accident) * 1000000 / record.heure_travailler
    
    class Meta:
        model = Performance_sante