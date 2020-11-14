# Generated by Django 3.1.2 on 2020-11-04 07:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sflightbook', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Flight',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('orgin', models.CharField(default=False, max_length=256)),
                ('destination', models.CharField(default=False, max_length=256)),
                ('company', models.CharField(default=False, max_length=256)),
                ('departure_date', models.DateField()),
                ('departure_time', models.TimeField()),
            ],
        ),
    ]