from django.urls import path

from iha.views import İhaList, İhaDetail

urlpatterns = [
    path('', İhaList.as_view()),
    path('<int:pk>/', İhaDetail.as_view()),
]
