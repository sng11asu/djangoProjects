from django.db import models

# Create your models here.
class Universitiesm(models.Model):
    alpha_two_code = models.CharField(max_length=2)
    country = models.CharField(max_length=20)
    domain = models.CharField(max_length=20)
    name = models.CharField(max_length=100)
    web_page = models.URLField()

    def __str__(self):
        return f"{self.name}"