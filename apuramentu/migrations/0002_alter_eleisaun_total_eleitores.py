# Generated by Django 4.0 on 2022-04-15 15:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apuramentu', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eleisaun',
            name='total_eleitores',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]