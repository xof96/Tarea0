from django.db import models


class Task(models.Model):
    name = models.CharField(max_length=200)
    priority = models.IntegerField(default=0)

    def __str__(self):
        return "Tarea: {}".format(self.name)
