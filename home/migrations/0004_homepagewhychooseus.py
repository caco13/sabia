# Generated by Django 3.1.4 on 2020-12-12 14:01

from django.db import migrations, models
import django.db.models.deletion
import modelcluster.fields


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_homepage_member_link'),
    ]

    operations = [
        migrations.CreateModel(
            name='HomePageWhyChooseUs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sort_order', models.IntegerField(blank=True, editable=False, null=True)),
                ('title', models.CharField(max_length=50, verbose_name='Título')),
                ('description', models.CharField(max_length=254, verbose_name='Description')),
                ('icon', models.CharField(blank=True, help_text='Fontawesome icon', max_length=100)),
                ('page', modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='why_choose_us', to='home.homepage')),
            ],
            options={
                'ordering': ['sort_order'],
                'abstract': False,
            },
        ),
    ]
