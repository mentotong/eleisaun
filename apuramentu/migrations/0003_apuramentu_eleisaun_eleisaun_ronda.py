# Generated by Django 4.0 on 2022-04-18 06:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('apuramentu', '0002_alter_eleisaun_total_eleitores'),
    ]

    operations = [
        migrations.AddField(
            model_name='apuramentu',
            name='eleisaun',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='apuramentu.eleisaun'),
        ),
        migrations.AddField(
            model_name='eleisaun',
            name='ronda',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
