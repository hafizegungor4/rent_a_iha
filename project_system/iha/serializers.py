from rest_framework import serializers
from .models import İha


class İhaSerializer(serializers.ModelSerializer):
    class Meta:
        model = İha
        fields = '__all__'
