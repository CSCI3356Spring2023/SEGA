# Generated by Django 4.1.7 on 2023-05-02 18:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('summary', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='application',
            name='Resume',
            field=models.FileField(blank=True, default='', upload_to='resumes'),
        ),
    ]
