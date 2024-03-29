# Generated by Django 4.1.7 on 2023-03-21 16:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('summary', '0002_course_tas'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='Description',
            field=models.CharField(max_length=2056, null=True),
        ),
        migrations.AddField(
            model_name='course',
            name='ExtraInfo',
            field=models.CharField(max_length=2056, null=True),
        ),
        migrations.AddField(
            model_name='course',
            name='GradedInMeeting',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='course',
            name='OfficeHours',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='course',
            name='WithDiscussion',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='course',
            name='TAs',
            field=models.IntegerField(null=True),
        ),
    ]
