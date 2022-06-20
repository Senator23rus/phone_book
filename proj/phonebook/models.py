from django.db import models

class Persone(models.Model):
    name = models.CharField("Contact name", max_length=50)
    def __str__(self):
        return self.name


