from django.urls import path
from .views_drf import PollList, PollDetail

urlpatterns = [
    path('polls/', PollList.as_view(), name='polls list'),
    path('polls/<int:pk>', PollDetail.as_view(), name='polls detail')
]
