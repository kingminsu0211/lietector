# Generated by Django 4.2.8 on 2024-01-05 18:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('voicephishing', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='voicephishingrecord',
            name='user',
        ),
    ]
