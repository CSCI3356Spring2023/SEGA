from django.db import models

# Create your models here.
class Course(models.Model):
    CourseID   = models.CharField(max_length=255)
    Name       = models.CharField(max_length=255)
    Instructor = models.CharField(max_length=255)
    SeatData   = models.CharField(max_length=255)
    Rooms      = models.CharField(max_length=255)
    Times      = models.CharField(max_length=255)
