from django.db import models


class Employees(models.Model):
    EmployeeId = models.AutoField(primary_key=True)
    EmployeeName = models.CharField(max_length=50)
    Salary = models.IntegerField()
    Bonus = models.IntegerField()
    PhoneNumber = models.CharField(max_length=10)
    Role = models.CharField(max_length=50)
    Department = models.CharField(max_length=50)
    Location = models.CharField(max_length=50)
    DateOfJoining = models.DateField()
