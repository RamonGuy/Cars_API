from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response 
from .serializers import CarSerializer
from rest_framework import status
from .models import Car
from cars import serializers

@api_view(['GET', 'POST'])
def cars_list(request):
    if request.method == 'GET':

        dealership_name = request.query_params.get('dealership')
        print(dealership_name)
        cars = Car.objects.all()

        if dealership_name:
            cars = cars.filter(dealership__name=dealership_name)

        serializer = CarSerializer(cars, many=True)
        return Response(serializer.data)
    elif request.method == "POST":
        serializer = CarSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'PUT', 'DELETE'])        
def car_detail(request, pk):
    car = get_object_or_404(Car, pk=pk)
    if request.method == 'GET':
        serializer = CarSerializer(car);
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = CarSerializer(car, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    elif request.method == 'DELETE':
        car.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

