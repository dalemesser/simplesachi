# Generated by Django 3.1.2 on 2020-11-06 06:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wiwaranatype', '0002_auto_20201105_1933'),
    ]

    operations = [
        migrations.AddField(
            model_name='wiwarana',
            name='ansewer',
            field=models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')], default=1, max_length=1),
        ),
    ]