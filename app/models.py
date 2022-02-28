from django.db import models

class Application(models.Model):
    host_name = models.CharField(max_length=200)

class EventSession(models.Model):
    session_id = models.CharField(max_length=100)


class Event(models.Model):

    class EventCategory(models.IntegerChoices):
        PAGE_INTERACTION = 0
        FORM_INTERACTION = 1

    application = models.ForeignKey(Application, on_delete=models.CASCADE)
    session = models.ForeignKey(EventSession, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    category = models.IntegerField(choices=EventCategory.choices)
    payload = models.JSONField()
    timestamp = models.DateTimeField()

