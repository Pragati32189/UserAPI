from django.db import models

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=100)
    useraddress = models.CharField(max_length=200)
    isActive = models.BooleanField(default=True)
    dateTimeModified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.username
    