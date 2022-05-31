from django.db import models


# Create your models here.

class Demand(models.Model):
    name = models.CharField(max_length=200, blank=True, null=True, default='')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta():
        db_table = 'demands'