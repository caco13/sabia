# Generated by Django 3.1.4 on 2021-02-24 21:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0006_auto_20210223_2012'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='price1x',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Price 1x'),
        ),
    ]
