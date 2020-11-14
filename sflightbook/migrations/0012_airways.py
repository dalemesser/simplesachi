# Generated by Django 3.1.2 on 2020-11-05 06:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sflightbook', '0011_auto_20201104_1913'),
    ]

    operations = [
        migrations.CreateModel(
            name='Airways',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('image', models.ImageField(upload_to='images/')),
                ('reg_no', models.CharField(max_length=5)),
                ('country', models.CharField(max_length=256)),
            ],
        ),
    ]
