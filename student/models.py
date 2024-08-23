from django.db import models
# from classroom.models import Classroom
from course.models import Course
from student_class.models import Student_Class

GENDER_CHOICES = (
    ('MALE', 'Male'),
    ('FEMALE', 'Female'),
    ('OTHER', 'Other'),
 )

class Student(models.Model):
    first_name = models.CharField(max_length=30, null=False)
    last_name = models.CharField(max_length=30, null=False)
    email = models.EmailField(null=False)
    phone_number = models.CharField(max_length=15, unique=True, blank=False)
    date_of_birth = models.DateField()
    code = models.PositiveSmallIntegerField(unique=True, null=False, blank=False)
    country = models.CharField(max_length=20, null=False, blank=False)
    profile = models.ImageField(upload_to='student_pictures/', null=True, blank=True)
    student_gender = models.CharField(max_length=6, choices=GENDER_CHOICES)
    bio = models.TextField(null=True)
    national_id = models.IntegerField(default=0)
    enrollment_date = models.DateField()
    end_date = models.DateField()
    parent = models.CharField(max_length=50)
    next_of_kin = models.CharField(max_length=50)
    parent_number = models.CharField(max_length=15)
    id = models.AutoField(primary_key=True)
    # classroom = models.OneToOneField(Classroom, on_delete=models.CASCADE)
    courses = models.ManyToManyField(Course)
    class_enrolled = models.ForeignKey(Student_Class, on_delete=models.SET_NULL, null=True, related_name='students')
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}"
