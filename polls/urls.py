from django.urls import path
from .views import polls_detail, polls_list

urlpatterns = [
    path('polls/', polls_list, name='polls list'),
    path('polls/<int:pk>', polls_detail, name='polls detail')
]
