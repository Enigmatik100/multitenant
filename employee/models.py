from django.db import models


class Employee(models.Model):
    age = models.IntegerField()
    name = models.CharField(max_length=100)
    created_at = models.DateField()

    class Meta:
        db_table = 'employees'
