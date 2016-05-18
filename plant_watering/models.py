from django.db import models
from django.utils import timezone

class Flower(models.Model):
  name = models.CharField(max_length=200)
  image = models.ImageField(default=None)
  last_watered = models.DateTimeField(
      default=timezone.now)
  water_period = models.PositiveSmallIntegerField()
