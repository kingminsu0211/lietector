# Generated by Django 4.2.8 on 2023-12-28 16:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first', '0002_alter_user_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='id',
            field=models.CharField(max_length=30, primary_key=True, serialize=False),
        ),
    ]
