# Generated by Django 4.1.7 on 2023-04-03 19:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('firstname', models.CharField(max_length=64)),
                ('lastname', models.CharField(max_length=64)),
                ('bcemail', models.CharField(max_length=64, unique=True)),
                ('password', models.CharField(max_length=64)),
                ('permissions', models.CharField(choices=[('STUDENT', 'Student'), ('INSTRUCTOR', 'Instructor'), ('ADMIN', 'Admin')], default='Student', max_length=16)),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CourseID', models.CharField(max_length=255)),
                ('Name', models.CharField(max_length=255)),
                ('Instructor', models.CharField(max_length=255)),
                ('Description', models.CharField(max_length=2056, null=True)),
                ('SeatData', models.CharField(max_length=255)),
                ('Rooms', models.CharField(max_length=255)),
                ('Times', models.CharField(max_length=255)),
                ('TAs', models.IntegerField(null=True)),
                ('WithDiscussion', models.IntegerField(null=True)),
                ('GradedInMeeting', models.IntegerField(null=True)),
                ('OfficeHours', models.IntegerField(null=True)),
                ('ExtraInfo', models.CharField(max_length=2056, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Admin',
            fields=[
                ('account_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='createcourse.account')),
                ('positions', models.CharField(max_length=255)),
            ],
            bases=('createcourse.account',),
        ),
        migrations.CreateModel(
            name='Instructor',
            fields=[
                ('account_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='createcourse.account')),
                ('position', models.CharField(max_length=255)),
            ],
            bases=('createcourse.account',),
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('account_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='createcourse.account')),
                ('year_in_school', models.CharField(choices=[('FR', 'Freshman'), ('SO', 'Sophomore'), ('JR', 'Junior'), ('SR', 'Senior'), ('GR', 'Graduate')], default='Freshman', max_length=2)),
                ('major', models.CharField(max_length=64)),
                ('eagleid', models.CharField(max_length=16)),
                ('work', models.CharField(choices=[('YES', 'Open to work'), ('NO', 'Not open to work')], default='NO', max_length=16)),
            ],
            bases=('createcourse.account',),
        ),
    ]
