from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=255)
    age = models.IntegerField()
    email = models.EmailField()
    roll_number = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.name} {self.age}"