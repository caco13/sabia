# Generated by Django 3.1.4 on 2020-12-29 10:49

from django.db import migrations, models
import django.db.models.deletion
import django_extensions.db.fields
import modelcluster.fields
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailtrans', '0009_create_initial_language'),
        ('base', '0008_coursematerial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CoursePage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('slug', django_extensions.db.fields.AutoSlugField(blank=True, editable=False, populate_from='title')),
            ],
            options={
                'verbose_name': 'Course page',
                'verbose_name_plural': 'Course page',
            },
        ),
        migrations.CreateModel(
            name='CoursePageItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sort_order', models.IntegerField(blank=True, editable=False, null=True)),
                ('description', wagtail.core.fields.RichTextField(blank=True, verbose_name='Descrição')),
                ('link_url', models.CharField(blank=True, help_text='URL to link to, e.g. /contato', max_length=254, null=True)),
                ('course_page', modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='course_page_items', to='base.coursepage')),
                ('link_page', models.ForeignKey(blank=True, help_text='Page to link to', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='wagtailtrans.translatablepage')),
            ],
            options={
                'ordering': ['sort_order'],
                'abstract': False,
            },
        ),
    ]
