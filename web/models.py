from django.db import models


class TaskModel(models.Model):
    name = models.CharField(max_length=20)
    details = models.CharField(max_length=100)
