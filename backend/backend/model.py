from django.db import models


class Cat(models.Model):
    name = models.CharField(max_length=120)
    title = models.CharField(max_length=120)

    def __str__(self):
        return self.name
