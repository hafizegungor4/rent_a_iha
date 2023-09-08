from django.urls import path
from rentstate.views import RentStateDetail, RentStateList

urlpatterns = [
    path('', RentStateList.as_view(), name='rentstate-list'),
    path('<int:pk>/', RentStateDetail.as_view(), name='rentstate-detail'),
]
