# Generated by Django 5.0.6 on 2024-05-12 00:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('djangoProject', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='schoolclasses',
            options={'ordering': ['id'], 'verbose_name': 'Класс', 'verbose_name_plural': 'Классы'},
        ),
    ]