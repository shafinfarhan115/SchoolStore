from django.db import models
from django.db.models.deletion import CASCADE


# Create your models here.

class Department(models.Model):
    departmentname = models.CharField(max_length=250)

    def __str__(self):
        return self.departmentname

class Course(models.Model):
    deptid = models.ForeignKey(Department, on_delete=CASCADE)
    course = models.CharField(max_length=250)

    def __str__(self):
        return self.course
class Order(models.Model):
    name = models.CharField(max_length=200)
    dob = models.DateField(default=None)
    age = models.IntegerField(default=None)
    gender = models.CharField(max_length=50, choices=(('Male', 'Male'), ('Female', 'Female'),))
    phone = models.CharField(max_length=10, default=None)
    email = models.EmailField()
    address = models.TextField(max_length=250)
    department = models.CharField(max_length=50)
    course = models.CharField(max_length=50)
    purpose = models.CharField(max_length=50)
    material = models.CharField(max_length=50)

    def __str__(self):
        return self.name