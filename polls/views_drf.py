from .models import Poll, Choice
from .serializers import PollSerializer, ChoiceSerializer, VoteSerializer

from rest_framework import generics


class PollList(generics.ListCreateAPIView):
        queryset = Poll.objects.all()
        serializer_class = PollSerializer


class PollDetail(generics.RetrieveDestroyAPIView):
        queryset = Poll.objects.all()
        serializer_class = PollSerializer


class ChoiceList(generics.ListCreateAPIView):
        def get_queryset(self):
                queryset = Choice.objects.filter(poll_id=self.kwargs["pk"])
                return queryset
        serializer_class = ChoiceSerializer


class CreateVote(generics.CreateAPIView):
        serializer_class = VoteSerializer
