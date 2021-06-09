import datetime

from django.db import models
from django.utils import timezone

class TimeStampMixin(models.Model):
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

  class Meta:
    abstract = True


class Title(TimeStampMixin):
  name = models.CharField(max_length=1000)
  release_year = models.IntegerField()

  def __str__(self):
    return self.name

  def was_added_recently(self):
    return self.created_at >= timezone.now() - datetime.timedelta(days=1)
