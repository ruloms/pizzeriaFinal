# Generated by Django 3.0.11 on 2021-06-13 17:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pizzeriaapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='complemento',
            name='precio',
            field=models.CharField(default='0', max_length=20),
        ),
        migrations.AddField(
            model_name='pizza',
            name='precio',
            field=models.CharField(default='0', max_length=20),
        ),
    ]
