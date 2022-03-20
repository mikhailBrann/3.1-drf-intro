from rest_framework import serializers
from measurement.models import Sensor, Measurement
# TODO: опишите необходимые сериализаторы


class SensorSeializer(serializers.ModelSerializer):
    """ сериализатор датчика """

    class Meta:
        model = Sensor
        fields = ['id', 'name', 'description']


class MeasurementSerializer(serializers.ModelSerializer):
    """ сериализатор состояния датчика """

    class Meta:
        model = Measurement
        fields = ['temperature', 'created_at']


class SensorDetailSerializer(serializers.ModelSerializer):
    """ суперсериализатор для детального вывода инфо о датчике """
    measurements = MeasurementSerializer(Sensor.measurements, read_only=True, many=True)

    class Meta:
        model = Sensor
        fields = ['id', 'name', 'description', 'measurements']