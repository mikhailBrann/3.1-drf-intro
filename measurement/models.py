from django.db import models

# TODO: опишите модели датчика (Sensor) и измерения (Measurement)


class Sensor(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=250, verbose_name='Описание датчика')

    class Meta:
        verbose_name = 'Датчик'

    def __str__(self):
        return self.name


class Measurement(models.Model):
    temperature = models.FloatField()
    created_at = models.DateField(auto_now_add=True)
    sensor = models.ManyToManyField(Sensor, related_name='sensor')
