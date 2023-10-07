import io

from car.models import Car
from car.serializers import CarSerializer
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer


def serialize_car_object(car: Car) -> bytes:
    serializer = CarSerializer(car)
    return JSONRenderer().render(serializer.data)


def deserialize_car_object(json: bytes) -> Car:
    file_txt = io.BytesIO(json)
    data = JSONParser().parse(file_txt)
    serializer = CarSerializer(data=data)
    if serializer.is_valid():
        return serializer.save()
