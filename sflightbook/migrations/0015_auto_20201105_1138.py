# Generated by Django 3.1.2 on 2020-11-05 06:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sflightbook', '0014_auto_20201105_1137'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flight',
            name='company',
            field=models.CharField(max_length=256),
        ),
        migrations.AlterField(
            model_name='flight',
            name='destination',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='arrivals', to='sflightbook.airport'),
        ),
    ]
