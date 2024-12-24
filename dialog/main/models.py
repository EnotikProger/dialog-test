from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator


class DeviceModel(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.name


class Device(models.Model):
    address = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    ip_address = models.CharField(
        max_length=15,
        validators=[RegexValidator(regex=r'^\d{1,3}(\.\d{1,3}){3}$', message='Invalid IP address')]
    )
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    device_model = models.ForeignKey(DeviceModel, on_delete=models.CASCADE)
    comments = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name
