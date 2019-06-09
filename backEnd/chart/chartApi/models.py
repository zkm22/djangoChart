from django.db import models
from django.utils import timezone

class Table1(models.Model):
  area = models.CharField(max_length=10)
  nth = models.IntegerField()
  value = models.IntegerField()
  def __str__(self):
    return ''

class Table2(models.Model):
  area1 = models.IntegerField()
  area2 = models.IntegerField()
  nth = models.IntegerField(default=0)
  dateTime = models.DateTimeField(default=timezone.now)
  def __str__(self):
    return ''
