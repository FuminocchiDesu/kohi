# Generated by Django 5.0.6 on 2024-09-17 14:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('KohiLocale', '0004_alter_userprofile_bio_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='favorite_coffee_shops',
        ),
    ]
