# Generated by Django 4.2.5 on 2023-10-05 07:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0018_checklist_permis_feu_prest_evacuation_substance'),
    ]

    operations = [
        migrations.AlterField(
            model_name='checklist_permis_feu_prest',
            name='evacuation_substance',
            field=models.BooleanField(default=False),
        ),
    ]
