# Generated by Django 4.2.8 on 2024-01-18 05:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('voicephishing', '0009_alter_diagnosis_audio_file_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='diagnosis',
            name='call_details',
            field=models.TextField(),
        ),
    ]
