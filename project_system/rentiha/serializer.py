from rest_framework import serializers

from rentstate.serializers import RentStateGetSerializer
from rentiha.models import RentIha
from project_system.urls import UserSerializer


class RentIhaGetSerializer(serializers.ModelSerializer):
    group = RentStateGetSerializer()
    member = UserSerializer()

    class Meta:
        model = RentIha
        fields = '__all__'


class RentIhaPostSerializer(serializers.ModelSerializer):

    class Meta:
        model = RentIha
        fields = '__all__'
