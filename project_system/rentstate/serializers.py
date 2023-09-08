from rest_framework import serializers
from rentstate.models import RentState
from rentiha.models import RentIha
from project_system.urls import UserSerializer
import uuid


class RentStateSerializer(serializers.ModelSerializer):
    member = UserSerializer()

    class Meta:
        model = RentIha
        fields = '__all__'

class RentStateGetSerializer(serializers.ModelSerializer):

    owner = UserSerializer()
    group_members = serializers.SerializerMethodField()
    group_projects = serializers.SerializerMethodField()

    def get_group_members(self, obj):
        group_members = RentIha.objects.filter(group_id=obj.id).all()
        return RentStateSerializer(group_members, many=True,
                                     context=self.context).data

    class Meta:
        model = RentState
        fields = '__all__'

class RentStatePostSerializer(serializers.ModelSerializer):
    invitation_code = serializers.ReadOnlyField()

    class Meta:
        model = RentState
        fields = '__all__'
        read_only_fields = ('id', 'owner', 'max_size', 'invitation_code')

    def create(self, validated_data):
        request = self.context.get('request')
        if request:
            validated_data['owner'] = request.user
        validated_data['invitation_code'] = str(uuid.uuid4())[:6].upper()
        return super().create(validated_data)
