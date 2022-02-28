from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotAllowed
from .tasks import parse_payload

# Create your views here.

def log_session(request):
    if request.method == "POST":
        posted_session = dict()
        posted_session = request.POST
        parse_payload.delay(posted_session)
        return HttpResponse({ "OK" : True})
    else:
        return HttpResponseNotAllowed(['POST'])