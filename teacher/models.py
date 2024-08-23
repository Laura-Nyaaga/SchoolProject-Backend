import datetime
from django.db import models
# from course.models import Course
GENDER_CHOICES = (
    ('MALE', 'Male'),
    ('FEMALE', 'Female'),
    ('OTHER', 'Other'),
 )
class Teacher(models.Model):
    first_name = models.CharField(max_length=30, null=False)
    last_name = models.CharField(max_length=30, null=False)
    email = models.EmailField(null=False)
    image = models.ImageField(null=True)
    date_of_birth = models.DateField(default=datetime.date.today)
    bio = models.TextField(null=True, blank=True)
    course = models.CharField(max_length=20)
    country = models.CharField(max_length=30)
    gender = models.CharField(max_length=6, choices=GENDER_CHOICES)
    phone_number = models.CharField(max_length=20)
    national_id = models.PositiveBigIntegerField(unique=True)
    account_number = models.PositiveIntegerField(unique=True, null=False)
    salary = models.DecimalField(max_digits=10, decimal_places=2, null=False, default= 0.00)
    department = models.CharField(max_length=30)
    id = models.AutoField(primary_key=True)
    # course = models.ManyToManyField(Course, on_delete=models.CASCADE, related_name='teachers')

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"



