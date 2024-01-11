# Generated by Django 4.2.8 on 2023-12-11 08:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Diagnosis',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('diagnosistype', models.TextField()),
                ('phonedetails', models.TextField()),
                ('diagnosisresults', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reportnumber', models.IntegerField()),
                ('reporttype', models.CharField(max_length=30)),
                ('reportdetails', models.TextField()),
                ('blockingdetails', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.CharField(max_length=30, primary_key=True, serialize=False, unique=True)),
                ('password', models.CharField(max_length=30)),
                ('nickname', models.CharField(max_length=30)),
                ('phonenumber', models.IntegerField()),
                ('reports', models.TextField()),
                ('blokings', models.TextField()),
            ],
        ),
    ]
