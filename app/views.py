from django.shortcuts import render
from django.http import JsonResponse, HttpResponseNotAllowed

# Create your views here.

def log_session(request):
    if request.method == "POST":
        payload = dict()
        payload = request.POST
        # TODO call function to process payload
        return JsonResponse({ "OK" : True})
    else:
        return HttpResponseNotAllowed(['POST'])