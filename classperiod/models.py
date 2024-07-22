
from django.db import models

from classroom.models import Classroom
from course.models import Course
from teacher.models import Teacher


class ClassPeriod(models.Model):
    start_time = models.TimeField(null=False, blank=False)
    end_time = models.TimeField(null=False, blank=False)  
    days_of_the_week = models.CharField(max_length=10,null=True, default='Monday')
    Course = models.CharField(max_length=30)
    course = models.ManyToManyField(Course, on_delete= models.CASCADE,related_name='classperiods')
    classroom = models.OneToOneField(Classroom, on_delete=models.CASCADE,  related_name='classperiods')
    teacher = models.OneToOneField(Teacher, on_delete=models.CASCADE, related_name='classperiods')


    def __str__(self):
        return f"{self.start_time}  {self.end_time}"
