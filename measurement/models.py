from django.db import models

# TODO: опишите модели датчика (Sensor) и измерения (Measurement)


class Measurement(models.Model):
    temperature = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)


class Sensor(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=250, verbose_name='Описание датчика')
    measurements = models.ManyToManyField(Measurement, related_name='measurements')
