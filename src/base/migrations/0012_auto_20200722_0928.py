# Generated by Django 3.0.7 on 2020-07-22 01:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0011_request'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='contact',
            options={'ordering': ['name'], 'verbose_name': 'Request Lesson', 'verbose_name_plural': 'Request Lesson'},
        ),
    ]
