from django.urls import path

from rentiha.views import RentIhaList, RentIhaDetail

urlpatterns = [
    path('', RentIhaList.as_view(), name='rentstate-member-list'),
    path('<int:pk>/', RentIhaDetail.as_view(), name='rentstate-member-detail'),
]
