# Generated by Django 3.2.4 on 2022-10-28 13:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('modulos', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='modulo',
            name='descricao',
            field=models.CharField(default='avenaria', max_length=100),
            preserve_default=False,
        ),
    ]
