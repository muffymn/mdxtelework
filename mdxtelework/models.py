from django.db import models

# Create your models here.
class Request(models.Model):
    placeholder = models.CharField(max_length=64)
    placeholder2 = models.CharField(max_length=64)
    placeholder3 = models.IntegerField()

    def __str__ (self):
        return f"{self.id}: {self.placeholder}: {self.placeholder2}: {self.placeholder3}"