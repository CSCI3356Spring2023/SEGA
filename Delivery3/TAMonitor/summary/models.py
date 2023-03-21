from django.db import models

class Course(models.Model):
    CourseID    = models.CharField(max_length=255)
    Name        = models.CharField(max_length=255)
    Instructor  = models.CharField(max_length=255)
    Description = models.CharField(max_length=2056, null=True)
    SeatData    = models.CharField(max_length=255)
    Rooms       = models.CharField(max_length=255)
    Times       = models.CharField(max_length=255)
    TAs = models.IntegerField(null=True)
    WithDiscussion = models.IntegerField(null=True)
    GradedInMeeting = models.IntegerField(null=True)
    OfficeHours = models.IntegerField(null=True)
    ExtraInfo   = models.CharField(max_length=2056, null=True)

    def __str__(self):
      return self.Name
