# Generated by Django 4.1.7 on 2023-05-01 14:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('summary', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='applications',
            field=models.ManyToManyField(blank=True, default='', to='summary.application'),
        ),
    ]