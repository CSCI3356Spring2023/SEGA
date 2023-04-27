from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager

class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        """Create and save a User with the given email and password."""
        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        """Create and save a regular User with the given email and password."""
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        """Create and save a SuperUser with the given email and password."""
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, password, **extra_fields)


class Account(AbstractUser):
    email = models.EmailField(('email address'), unique=True)
    firstname = models.CharField(max_length=64)
    lastname = models.CharField(max_length=64)
    password = models.CharField(max_length=64)
    is_student = models.BooleanField(default=False)
    is_instructor = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['firstname', 'lastname', 'password']

    objects = UserManager()

    def __str__(self):
      return self.email



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
    WithDiscussion = models.CharField(max_length=255)
    GradedInMeeting = models.CharField(max_length=255)
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
    work = models.CharField(max_length=16, choices=OPEN_TO_WORK, default='Open to work')

    def __str__(self):
      return self.email

class Instructor(Account):
    position = models.CharField(max_length=255) # e.g CS Professor

    def __str__(self):
      return self.email

class Admin(Account):
    position = models.CharField(max_length=255) # e.g IT Admin

    def __str__(self):
      return self.email
