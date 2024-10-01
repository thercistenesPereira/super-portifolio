from django.db import models


# Create your models here.
class Profile(models.Model):
    name = models.CharField(max_length=200)
    github = models.URLField(max_length=200)
    linkedin = models.URLField(max_length=200)
    bio = models.TextField(max_length=2000)

    def __str__(self):
        return self.name
