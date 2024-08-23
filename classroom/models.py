from django.db import models
# from teacher.models import Teacher

class Classroom(models.Model):
    name = models.CharField(max_length=20)
    classroom_id = models.PositiveIntegerField(null = False)
    description = models.TextField(null=True)
    capacity = models.PositiveSmallIntegerField(default=00)
    equipments = models.TextField(null=False)
    # teacher = models.ManyToManyField(Teacher, on_delete=models.CASCADE, related_name='classrooms')

    def __str__(self):
        return f"{self.name}  {self.capacity}"

