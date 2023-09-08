from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rentstate.models import RentState
from rentstate.serializers import RentStateGetSerializer, RentStatePostSerializer


class RentStateList(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = RentState.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return RentStateGetSerializer
        return RentStatePostSerializer


class RentStateDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = RentState.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return RentStateGetSerializer
        return RentStatePostSerializer
