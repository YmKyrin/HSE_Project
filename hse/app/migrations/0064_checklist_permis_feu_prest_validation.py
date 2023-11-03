# Generated by Django 4.2.5 on 2023-11-02 06:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0063_remove_checklist_permis_feu_prest_validation'),
    ]

    operations = [
        migrations.AddField(
            model_name='checklist_permis_feu_prest',
            name='validation',
            field=models.CharField(choices=[('en_attente', 'En attente de réponse'), ('confirme', 'Confirmé'), ('refuse', 'Refusé')], default='en_attente', max_length=15),
        ),
    ]
