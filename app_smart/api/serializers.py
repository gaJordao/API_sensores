from django.contrib.auth.models import User
from rest_framework import serializers
from django.contrib.auth.hashers import make_password
from app_smart.models import Sensor, TemperaturaData, UmidadeData, ContadorData, LuminosidadeData
from rest_framework import viewsets


class UserSerializer(serializers.ModelSerializer):

    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data['password'])
        return super().create(validated_data)


    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password']
        extra_kwargs = {'password': {'write_only': True}}

class SensorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sensor
        fields = '__all__'


class TemperaturaDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = TemperaturaData
        fields = '__all__'

class UmidadeDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = UmidadeData
        fields = '__all__'

class ContadorDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContadorData 
        fields = '__all__'

class LuminosidadeDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = LuminosidadeData 
        fields = '__all__'


