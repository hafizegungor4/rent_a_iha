from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response

from iha.models import İha
from iha.serializers import İhaSerializer
from project_system.permissions import ReadOnly


# Create your views here.
class İhaList(generics.ListCreateAPIView):
    permission_classes = [IsAdminUser]
    queryset = İha.objects.all()
    serializer_class = İhaSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


class İhaDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated | ReadOnly]
    queryset = İha.objects.all()
    serializer_class = İhaSerializer
