# Generated by Django 3.1.2 on 2020-11-04 08:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sflightbook', '0005_airport'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flight',
            name='orgin',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sflightbook.airport'),
        ),
    ]
