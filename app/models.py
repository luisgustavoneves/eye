from django.db import models

class Application(models.Model):
    host_name = models.CharField(max_length=200)

class EventSession(models.Model):
    session_id = models.CharField(max_length=100)

class EventCategory(models.IntegerChoices):
    PAGE_INTERACTION = 0, 'page interaction'
    FORM_INTERACTION = 1, 'form interaction'

class Event(models.Model):
    application = models.ForeignKey(Application)
    session = models.ForeignKey(EventSession)
    category = models.IntegerChoices(choices=EventCategory.choices)
    payload = models.JSONField()
    timestamp = models.DateTimeField()

