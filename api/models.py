from django.db import models

# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=100)
    nickName = models.CharField(max_length=50)
    age = models.PositiveSmallIntegerField()
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name