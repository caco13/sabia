# Generated by Django 3.1.4 on 2021-01-23 21:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0004_auto_20210117_1628'),
    ]

    operations = [
        migrations.AddField(
            model_name='teammember',
            name='order',
            field=models.IntegerField(blank=True, default=10, verbose_name='Posição'),
        ),
    ]
