from rest_framework import serializers
from oemsapp.models import Employees


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employees
        fields = ('EmployeeId', 'EmployeeName', 'Salary', 'Bonus', 'PhoneNumber', 'Role', 'Department',
                  'Location', 'DateOfJoining')
