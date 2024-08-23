import datetime
from django.db import models
# from classroom.models import Classroom
from student_class.models import Student_Class
from teacher.models import Teacher


class Course(models.Model):
    id = models.AutoField(primary_key=True)
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
    teacher = models.ForeignKey(Teacher, on_delete=models.SET_NULL, null=True, related_name='courses')
    classes = models.ManyToManyField(Student_Class, related_name='courses')


    def __str__(self):
        return f"{self.name}"
