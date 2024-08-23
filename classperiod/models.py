
from django.db import models

# from classroom.models import Classroom
from course.models import Course
from student_class.models import Student_Class
# from teacher.models import Teacher


class ClassPeriod(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    start_time = models.TimeField(null=False, blank=False)
    end_time = models.TimeField(null=False, blank=False)  
    days_of_the_week = models.CharField(max_length=10,null=True, default='Monday')
    created_at = models.DateField()
    updated_at = models.DateField()
    # Course = models.CharField(max_length=30)
    course = models.ForeignKey(Course, on_delete= models.SET_NULL, null=True, related_name='student_class')
    student_class = models.ForeignKey(Student_Class, on_delete=models.SET_NULL, null=True, related_name='course')
    # classroom = models.OneToOneField(Classroom, on_delete=models.CASCADE,  related_name='classperiods')
    # teacher = models.OneToOneField(Teacher, on_delete=models.CASCADE, related_name='classperiods')


    def __str__(self):
        return f"{self.name}"
