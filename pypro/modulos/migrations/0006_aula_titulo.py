# Generated by Django 3.2.4 on 2022-10-28 13:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('modulos', '0005_aula_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='aula',
            name='titulo',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
