from celery import shared_task
from datetime import datetime
from app.models import *
from celery.utils.log import get_task_logger

logger = get_task_logger(__name__)

categories = { "page interaction": 0, "form interaction":1}

@shared_task
def parse_payload(posted_session):

    try:
        session_id = posted_session[0]["session_id"]
        host = posted_session[0]["data"]["host"]
    except:
        #log invalid session
        logger.error('invalid session')
        return

    session = EventSession.get_or_create(session_id=session_id)

    application = Application.get_or_create(host=host)
    
    for event in posted_session:
        
        if session_id != event["session_id"]:
            # log invalid event
            logger.error('invalid event, different session_id')
            continue

        try:
            category= categories[event["category"]]
            name = event["name"]
            timestamp = datetime.timestamp(event["timestamp"])
            if timestamp > datetime.now():
                # log future event
                logger.error("invalid event, future timestamp")
                continue
            payload = event["data"]
        except:
            # log invalid event 
            logger.error("invalid event, missing category, name or timestamp")
            continue

        new_event = Event(application=application, session=session, name=name, category=category, timestamp=timestamp, payload=payload)
        new_event.save()