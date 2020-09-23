from django.db import models

# Create your models here.
class Credential(models.Model):
    name = models.CharField(max_length=30, default="")
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
    url = models.CharField(max_length=255, default="")
    def __str__(self):
        return self.name