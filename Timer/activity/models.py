from django.db import models
from django.contrib.auth.models import User


class Activities(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    activity = models.CharField(max_length=250)
    date = models.DateField()
    duration = models.CharField(max_length=50, default=0)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.activity
