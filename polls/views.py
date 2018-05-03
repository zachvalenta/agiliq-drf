from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404
from polls.models import Poll


def polls_list(request):
    polls = Poll.objects.all()
    data = {"results": list(polls.values("text", "user_id__username", "pub_date"))}
    return JsonResponse(data)

# JsonResponse = HttpResponse w/ content-type = JSON
# accessing related obj notation (`user_id__username` vs. `user_id.username`)

def polls_detail(request, pk):
    poll = get_object_or_404(Poll, pk=pk)
    data = {"results": {
        "text": poll.text,
        "user_id": poll.user_id.username,
        "pub_date": poll.pub_date
    }}
    return JsonResponse(data)
