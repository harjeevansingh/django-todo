from django.db import models


class Task(models.Model):
    title = models.CharField(max_length=200)
    date = models.DateField()
    time = models.TimeField()
    description = models.TextField()
    location = models.CharField(max_length=200)

    def __str__(self):
        return self.title

