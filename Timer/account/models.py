from django.db import models
from django.conf import settings


class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    address = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return 'Profile for user {}'.format(self.user)

