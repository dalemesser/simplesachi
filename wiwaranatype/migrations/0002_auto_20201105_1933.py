# Generated by Django 3.1.2 on 2020-11-05 14:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wiwaranatype', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wiwarana',
            name='year',
            field=models.CharField(choices=[('2020', '2020'), ('2019', '2019')], max_length=4),
        ),
    ]
