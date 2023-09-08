from django.urls import path
from rent_iha_report.views \
    import RentIhaReportList, \
    RentIhaReportDetail

urlpatterns = [
    path('', RentIhaReportList.as_view()),
    path('<int:pk>/', RentIhaReportDetail.as_view()),
]
