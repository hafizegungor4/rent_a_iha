from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rentiha.models import RentIha
from rentiha.serializer import RentIhaGetSerializer,\
    RentIhaPostSerializer


class RentIhaList(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = RentIha.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return RentIhaGetSerializer
        return RentIha


class RentIhaDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = RentIha.objects.all()
    serializer_class = RentIhaGetSerializer

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return RentIhaGetSerializer
        return RentIhaPostSerializer
