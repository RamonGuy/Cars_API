from logging.handlers import DEFAULT_HTTP_LOGGING_PORT
from rest_framework import serializers
from .models import Car

class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = ['id', 'make', 'model', 'year', 'price', 'dealership']
        depth=1