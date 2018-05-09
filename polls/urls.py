from django.urls import path
from .views_drf import PollList, PollDetail, ChoiceList, CreateVote

urlpatterns = [
    path('polls/', PollList.as_view(), name='polls list'),
    path('polls/<int:pk>', PollDetail.as_view(), name='polls detail'),
    path('polls/<int:pk>/choices', ChoiceList.as_view(), name='choice list'),
    path('votes/', CreateVote.as_view(), name='create vote')
]
