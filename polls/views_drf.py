from .models import Poll
from .serializers import PollSerializer

from rest_framework import generics


class PollList(generics.ListCreateAPIView):
        queryset = Poll.objects.all()
        serializer_class = PollSerializer


class PollDetail(generics.RetrieveDestroyAPIView):
        queryset = Poll.objects.all()
        serializer_class = PollSerializer
