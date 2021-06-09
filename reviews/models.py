from django.db import models


class TimeStampMixin(models.Model):
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

  class Meta:
    abstract = True


class Title(TimeStampMixin):
  name = models.CharField(max_length=1000)
  release_year = models.IntegerField()
