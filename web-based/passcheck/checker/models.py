from django.db import models


class Device(models.Model):
    device_name = models.CharField(max_length=50)

