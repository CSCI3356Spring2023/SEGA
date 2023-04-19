from django.db import models

class Account(models.Model):
    PERMISSIONS = [
        ('STUDENT', 'Student'),
        ('INSTRUCTOR', 'Instructor'),
        ('ADMIN', 'Admin'),
    ]

    firstname = models.CharField(max_length=64)
    lastname = models.CharField(max_length=64)
    bcemail = models.CharField(max_length=64, unique=True)
    password = models.CharField(max_length=64)
    permissions = models.CharField(max_length=16, choices=PERMISSIONS, default='Student')

    def __str__(self):
      return self.bcemail



class Application(models.Model):
    user = models.ForeignKey(Account, on_delete=models.CASCADE, primary_key=False)
    SelectedCourse = models.CharField(max_length=255)
    Experience = models.CharField(max_length=4096)
    Resume = models.FileField(default='', blank=True)

    def __str__(self):
        return 'TA-Application-' + str(self.id) + '-' + self.CourseName

class Course(models.Model):
    CourseID    = models.CharField(max_length=255)
    Name        = models.CharField(max_length=255)
    Instructor  = models.CharField(max_length=255)
    Description = models.CharField(max_length=2056, null=True)
    SeatData    = models.CharField(max_length=255)
    Rooms       = models.CharField(max_length=255)
    Times       = models.CharField(max_length=255)
    TAs = models.IntegerField(null=True)
    WithDiscussion = models.BooleanField(default = "Yes")
    GradedInMeeting = models.BooleanField(default = "Yes")
    OfficeHours = models.CharField(max_length=255, null=True)
    ExtraInfo   = models.CharField(max_length=2056, null=True)
    Applications = models.ManyToManyField(Application, default='', blank=True)

    def __str__(self):
      return self.CourseID

class Student(Account):
    YEAR_IN_SCHOOL = [
        ('FR', 'Freshman'),
        ('SO', 'Sophomore'),
        ('JR', 'Junior'),
        ('SR', 'Senior'),
        ('GR', 'Graduate'),
    ]

    year_in_school = models.CharField(
        max_length=2,
        choices=YEAR_IN_SCHOOL,
        default='Freshman',
    )

    OPEN_TO_WORK = [
        ('YES', 'Open to work'),
        ('NO', 'Not open to work'),
    ]

    major = models.CharField(max_length=64)
    eagleid = models.CharField(max_length=16)
    work = models.CharField(max_length=16, choices=OPEN_TO_WORK, default='NO')

    def __str__(self):
      return self.bcemail

class Instructor(Account):
    position = models.CharField(max_length=255) # e.g CS Professor

    def __str__(self):
      return self.bcemail

class Admin(Account):
    position = models.CharField(max_length=255) # e.g IT Admin

    def __str__(self):
      return self.bcemail
