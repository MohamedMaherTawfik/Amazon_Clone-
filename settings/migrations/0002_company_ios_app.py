# Generated by Django 4.2 on 2024-03-21 04:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('settings', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='ios_app',
            field=models.URLField(blank=True, null=True),
        ),
    ]
