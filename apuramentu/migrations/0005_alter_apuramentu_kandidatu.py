# Generated by Django 4.0 on 2022-04-18 06:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('apuramentu', '0004_kandidatu_numeru_sorteiu'),
    ]

    operations = [
        migrations.AlterField(
            model_name='apuramentu',
            name='kandidatu',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='kandidatu', to='apuramentu.kandidatu'),
        ),
    ]
