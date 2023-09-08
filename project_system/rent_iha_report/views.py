from rest_framework import generics

from rest_framework.permissions import IsAdminUser, IsAuthenticated

from project_system.permissions import ReadOnly
from rent_iha_report.models import RentIhaReport
from rent_iha_report.serializers \
    import RentIhaReportGetSerializer, \
    RentIhaReportPostSerializer


# Create your views here.
class RentIhaReportList(generics.ListCreateAPIView):
    permission_classes = [ReadOnly | IsAdminUser]

    def get_queryset(self):
        if self.request.user.is_staff or self.request.user.is_superuser:
            return RentIhaReport.objects.all()
        return RentIhaReport.objects.filter(member=self.request.user)

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return RentIhaReportGetSerializer
        return RentIhaReportPostSerializer


class RentIhaReportDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated | ReadOnly | IsAdminUser]
    serializer_class = RentIhaReportGetSerializer

    def get_queryset(self):
        if self.request.user.is_staff or self.request.user.is_superuser:
            return RentIhaReport.objects.all()
        return RentIhaReport.objects.filter(member=self.request.user)

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return RentIhaReportGetSerializer
        return RentIhaReportPostSerializer
