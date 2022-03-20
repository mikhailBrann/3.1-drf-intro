# TODO: опишите необходимые обработчики, рекомендуется использовать generics APIView классы:
# TODO: ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView
from rest_framework.decorators import api_view
from rest_framework.generics import ListCreateAPIView, RetrieveAPIView, CreateAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from measurement.models import Sensor, Measurement
from measurement.serializers import SensorSeializer, SensorDetailSerializer

# @api_view(['GET', 'POST'])
# def test(request):
#     if request.method == 'GET':
#         sensors = Sensor.objects.all()
#         sensors_serialize = SensorSeializer(sensors, many=True)
#         return Response(sensors_serialize.data)
#     if request.method == 'POST':
#         ...


# class SensorView(APIView):
#     def get(self, request):
#         sensors = Sensor.objects.all()
#         sensors_serialize = SensorSeializer(sensors, many=True)
#         return Response(sensors_serialize.data)
#
#     def post(self, request):
#         return Response({'status': 'ok'})

class SensorExists():
    def _sensor_exist(self, pk):
        current_sensor = False

        if Sensor.objects.all().filter(id=pk).exists():
            current_sensor = Sensor.objects.get(id=pk)

        return current_sensor


class SensorsView(ListCreateAPIView):
    queryset = Sensor.objects.all().order_by('id')
    serializer_class = SensorSeializer

    def post(self, request):
        if 'name' in request.data and 'description' in request.data:
            new_sensor = Sensor(name=request.data['name'], description=request.data['description']).save()
            return Response({'status': f"sensor {request.data['name']} - successfully registered!"})


class SensorView(RetrieveAPIView, SensorExists):

    def get(self, request, pk):
        sensor = self._sensor_exist(pk)

        if sensor:
            serializer_class = SensorDetailSerializer(sensor)
            print(serializer_class.data)
            return Response(serializer_class.data)

        else:
            return Response({"status": f"sensor {pk} not exist"})

    def patch(self, request, pk):
            sensor = self._sensor_exist(pk)

            if sensor:
                if 'name' in request.data:
                    sensor.name = request.data['name']
                if 'description' in request.data:
                    sensor.description = request.data['description']

                sensor.save()
                return Response({"status": f"{sensor.name} - successfully updated"})

            else:
                return Response({"status": f"sensor {pk} not exist"})


class MeasurementView(CreateAPIView, SensorExists):

    def post(self, request):
        current_sensor = self._sensor_exist(request.data['sensor'])

        if current_sensor:
            data_for_sensor = Measurement(temperature=request.data['temperature'])
            data_for_sensor.save()
            data_for_sensor.sensor.add(current_sensor)
            return Response({"status": f"ok"})

        else:
            return Response({"status": f"sensor {request.data['sensor']} not exist"})