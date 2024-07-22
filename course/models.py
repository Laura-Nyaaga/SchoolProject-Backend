import datetime
from django.db import models
from classroom.models import Classroom
from teacher.models import Teacher


class Course(models.Model):
    name = models.CharField(max_length=30, unique=True)
    description = models.CharField(max_length=100)
    fee = models.DecimalField(max_digits=10, decimal_places=2, default=0.00, null=True)
    course_code = models.CharField(max_length=5, null=False, unique=True)
    content = models.TextField(null=False, blank=False)
    start_date = models.DateField(datetime.date.today)
    end_date = models.DateField(datetime.date.today)
    course_duration = models.DurationField(default=1)
    department = models.CharField(max_length=30)
    number_of_students = models.PositiveSmallIntegerField(default=0)
    teacher = models.ManyToManyField(Teacher, on_delete=models.CASCADE, related_name='courses')
    classroom = models.OneToOneField(Classroom,on_delete=models.CASCADE, primary_key=True, related_name='courses')


    def __str__(self):
        return f"{self.name}, {self.course_code}"
