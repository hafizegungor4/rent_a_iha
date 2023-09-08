from rest_framework import serializers

from project_system.urls import UserSerializer
from rentiha.serializer import RentIhaGetSerializer
from rent_iha_report.models import RentIhaReport


class RentIhaReportGetSerializer(serializers.ModelSerializer):
    iha = RentIhaGetSerializer()
    member = UserSerializer()

    class Meta:
        model = RentIhaReport
        fields = '__all__'


class RentIhaReportPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = RentIhaReport
        fields = '__all__'
