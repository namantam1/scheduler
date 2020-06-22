from django.db import models

# Create your models here.
class Schedule(models.Model):
    url = models.URLField()
    datetime = models.DateTimeField()

    def __str__(self):
        return f'{self.url}'
