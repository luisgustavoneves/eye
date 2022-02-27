#import requests
from celery import shared_task

from app.models import *

@shared_task
def parse_payload(payload):

    for event in payload:
        session_id = event["session_id"]
        category =  event["category"]
        name = event["name"]