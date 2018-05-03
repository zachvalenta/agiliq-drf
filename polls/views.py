from django.http import HttpResponse


def polls_list(request):
    return HttpResponse("hi from polls_list")


def polls_detail(request, pk):
    return HttpResponse('poll detail {}'.format(pk))
