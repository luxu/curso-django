# Generated by Django 3.2.4 on 2022-10-28 13:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('modulos', '0004_auto_20221028_1052'),
    ]

    operations = [
        migrations.AddField(
            model_name='aula',
            name='slug',
            field=models.SlugField(null=True, unique=True),
        ),
    ]
