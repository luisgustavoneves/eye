from django.shortcuts import render
from django.http import JsonResponse, HttpResponseNotAllowed
from .tasks import parse_payload

# Create your views here.

def log_session(request):
    if request.method == "POST":
        posted_session = dict()
        posted_session = request.POST
        # TODO call function to process payload
        parse_payload.delay(posted_session)
        return JsonResponse({ "OK" : True})
    else:
        return HttpResponseNotAllowed(['POST'])